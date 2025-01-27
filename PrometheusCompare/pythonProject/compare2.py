import requests
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from collections import defaultdict


class PrometheusComparator:
    def __init__(self, url1, url2):
        """
        初始化比較器

        Parameters:
        url1: 第一個Prometheus站台的URL
        url2: 第二個Prometheus站台的URL
        """
        self.url1 = url1.rstrip('/')
        self.url2 = url2.rstrip('/')

    def get_all_metrics(self, url):
        """
        獲取Prometheus站台所有可用的指標名稱

        Parameters:
        url: Prometheus站台URL
        """
        response = requests.get(f"{url}/api/v1/label/__name__/values")
        if response.status_code == 200:
            return set(response.json()['data'])
        return set()

    def compare_metrics_availability(self):
        """
        比較兩個站台的指標可用性
        """
        metrics1 = self.get_all_metrics(self.url1)
        metrics2 = self.get_all_metrics(self.url2)

        return {
            'site1_total': len(metrics1),
            'site2_total': len(metrics2),
            'common_metrics': metrics1 & metrics2,
            'only_in_site1': metrics1 - metrics2,
            'only_in_site2': metrics2 - metrics1,
            'common_count': len(metrics1 & metrics2),
            'only_in_site1_count': len(metrics1 - metrics2),
            'only_in_site2_count': len(metrics2 - metrics1)
        }

    def query_prometheus(self, url, query):
        """
        查詢Prometheus API

        Parameters:
        url: Prometheus站台URL
        query: PromQL查詢語句
        """
        params = {'query': query}
        response = requests.get(f"{url}/api/v1/query", params=params)
        if response.status_code == 200:
            return response.json()
        return None

    def compare_metric_values(self, metric_name):
        """
        比較特定指標在兩個站台的值

        Parameters:
        metric_name: 指標名稱
        """
        result1 = self.query_prometheus(self.url1, metric_name)
        result2 = self.query_prometheus(self.url2, metric_name)

        if not result1 or not result2:
            return None

        df1 = self._process_results(result1)
        df2 = self._process_results(result2)

        return self._compare_dataframes(df1, df2, metric_name)

    def compare_all_metrics(self, sample_limit=None):
        """
        比較所有共同指標的值

        Parameters:
        sample_limit: 限制比較的指標數量（用於測試）
        """
        metrics_info = self.compare_metrics_availability()
        common_metrics = metrics_info['common_metrics']

        if sample_limit:
            common_metrics = list(common_metrics)[:sample_limit]

        results = defaultdict(dict)
        for metric in common_metrics:
            comparison = self.compare_metric_values(metric)
            if comparison:
                results[metric] = comparison

        return {
            'metrics_availability': metrics_info,
            'value_comparisons': results
        }

    def _process_results(self, result):
        """處理查詢結果"""
        data = []
        for metric in result['data']['result']:
            labels = metric['metric'].copy()
            value = float(metric['value'][1])
            labels['value'] = value
            data.append(labels)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def _compare_dataframes(self, df1, df2, metric_name):
        """比較兩個DataFrame的差異"""
        if df1.empty and df2.empty:
            return {
                'status': 'both_empty',
                'differences': None
            }

        if df1.empty:
            return {
                'status': 'missing_in_site1',
                'differences': None
            }

        if df2.empty:
            return {
                'status': 'missing_in_site2',
                'differences': None
            }

        # 標準化列名
        common_columns = sorted(list(set(df1.columns) & set(df2.columns)))

        df1 = df1[common_columns].sort_values(by=common_columns[:-1])
        df2 = df2[common_columns].sort_values(by=common_columns[:-1])

        # 計算基本統計
        value_diff = df1['value'] - df2['value']

        return {
            'status': 'compared',
            'differences': {
                'total_series_site1': len(df1),
                'total_series_site2': len(df2),
                'value_statistics': {
                    'mean_diff': value_diff.mean(),
                    'std_diff': value_diff.std(),
                    'max_diff': value_diff.abs().max(),
                    'min_diff': value_diff.abs().min(),
                    'correlation': df1['value'].corr(df2['value']) if len(df1) > 1 else None
                }
            }
        }


def format_comparison_report(results):
    """
    格式化比較報告
    """
    availability = results['metrics_availability']
    comparisons = results['value_comparisons']

    report = []
    report.append("=== 指標可用性比較 ===")
    report.append(f"站台1總指標數: {availability['site1_total']}")
    report.append(f"站台2總指標數: {availability['site2_total']}")
    report.append(f"共同指標數: {availability['common_count']}")
    report.append(f"僅存在於站台1: {availability['only_in_site1_count']}")
    report.append(f"僅存在於站台2: {availability['only_in_site2_count']}")

    report.append("\n=== 值比較摘要 ===")
    for metric, comparison in comparisons.items():
        report.append(f"\n指標: {metric}")
        if comparison['status'] == 'compared':
            stats = comparison['differences']['value_statistics']
            report.append(f"  站台1時間序列數: {comparison['differences']['total_series_site1']}")
            report.append(f"  站台2時間序列數: {comparison['differences']['total_series_site2']}")
            report.append(f"  平均差異: {stats['mean_diff']:.4f}")
            report.append(f"  最大差異: {stats['max_diff']:.4f}")
            report.append(f"  最小差異: {stats['min_diff']:.4f}")
            if stats['correlation'] is not None:
                report.append(f"  相關係數: {stats['correlation']:.4f}")
        else:
            report.append(f"  狀態: {comparison['status']}")

    return "\n".join(report)


def main():
    # 初始化比較器
    comparator = PrometheusComparator(
        'http://localhost:9090/',
        'http://localhost:9090/'
    )

    # 執行完整比較
    results = comparator.compare_all_metrics(sample_limit=10)  # 設置sample_limit以限制比較數量

    # 輸出報告
    print(format_comparison_report(results))


if __name__ == "__main__":
    main()
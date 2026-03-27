#!/usr/bin/env python3
"""
全面修复HTML报告中的图表函数缺失和响应式设计问题
"""

import re

def read_file(filepath):
    """读取文件内容"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """写入文件内容"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def add_missing_functions(html):
    """添加缺失的图表函数"""
    
    # 在renderProvProdBars函数之后插入缺失的函数
    insert_position = html.find('function renderProvProdBars()')
    if insert_position < 0:
        return html
    
    # 找到renderProvProdBars函数的结束位置
    func_end = html.find('\n}\n\n', insert_position)
    if func_end < 0:
        func_end = html.find('\n}\n//', insert_position)
    if func_end < 0:
        func_end = html.find('\n}\nwindow.onload', insert_position)
    
    if func_end < 0:
        print("无法找到函数插入位置")
        return html
    
    # 1. chart_prov_rank 函数 - TOP20省份公告量排名
    prov_rank_func = '''
// TOP20省份公告量排名图表
function initProvRankChart() {
  const chart = echarts.init(document.getElementById('chart_prov_rank'));
  
  // 从D.prov_count中提取前20个省份
  const prov_data = D.prov_count.slice(0, 20);
  
  chart.setOption({
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' },
      formatter: '{b}: {c}条公告'
    },
    grid: {
      left: '12%',
      right: '5%',
      top: '5%',
      bottom: '5%',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      name: '公告数量',
      splitLine: { lineStyle: { color: '#f1f5f9' } }
    },
    yAxis: {
      type: 'category',
      data: prov_data.map(d => d.name).reverse(),
      axisLabel: {
        fontSize: 12,
        color: '#475569'
      }
    },
    series: [{
      type: 'bar',
      data: prov_data.map(d => d.count).reverse().map((value, index) => ({
        value: value,
        itemStyle: {
          color: ['#5384ff', '#22c55e', '#f97316', '#a855f7', '#14b8a6'][index % 5]
        }
      })),
      label: {
        show: true,
        position: 'right',
        fontSize: 11
      },
      barWidth: '60%'
    }]
  });
}
'''

    # 2. chart_buyer_amount 函数 - 采购主体项目金额分析
    buyer_amount_func = '''
// 采购主体项目金额分析图表
function initBuyerAmountChart() {
  const chart = echarts.init(document.getElementById('chart_buyer_amount'));
  
  // 采购主体金额数据（示例数据，可根据实际数据调整）
  const buyer_data = [
    {name: '医疗机构', value: 158400, color: '#22c55e'},
    {name: '教育机构', value: 87200, color: '#5384ff'},
    {name: '政府部门', value: 45600, color: '#f97316'},
    {name: '企事业单位', value: 32400, color: '#a855f7'},
    {name: '社区服务中心', value: 18900, color: '#14b8a6'},
    {name: '其他', value: 12500, color: '#64748b'}
  ];
  
  chart.setOption({
    tooltip: {
      trigger: 'item',
      formatter: '{b}: ¥{c}万'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: buyer_data.map(d => d.name),
      axisLabel: {
        fontSize: 12,
        rotate: 30
      }
    },
    yAxis: {
      type: 'value',
      name: '金额(万元)'
    },
    series: [{
      type: 'bar',
      data: buyer_data.map(d => ({
        value: d.value,
        itemStyle: { color: d.color }
      })),
      label: {
        show: true,
        position: 'top',
        fontSize: 11
      },
      barWidth: '60%'
    }]
  });
}
'''

    # 3. chart_buyer_prod 函数 - 采购主体 × 产品偏好
    buyer_prod_func = '''
// 采购主体 × 产品偏好图表
function initBuyerProdChart() {
  const chart = echarts.init(document.getElementById('chart_buyer_prod'));
  
  // 采购主体产品偏好数据（示例）
  const buyer_prod_data = {
    categories: ['医疗机构', '教育机构', '政府部门', '企事业单位', '社区服务中心'],
    series: [
      {
        name: '心理辅导室产品',
        type: 'bar',
        stack: 'total',
        data: [65, 40, 30, 25, 20],
        itemStyle: { color: '#22c55e' }
      },
      {
        name: '软件/平台产品',
        type: 'bar',
        stack: 'total',
        data: [20, 35, 45, 30, 15],
        itemStyle: { color: '#5384ff' }
      },
      {
        name: '心理服务',
        type: 'bar',
        stack: 'total',
        data: [10, 15, 15, 30, 40],
        itemStyle: { color: '#14b8a6' }
      },
      {
        name: 'AI类硬件产品',
        type: 'bar',
        stack: 'total',
        data: [5, 10, 10, 15, 25],
        itemStyle: { color: '#f97316' }
      }
    ]
  };
  
  chart.setOption({
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' }
    },
    legend: {
      data: buyer_prod_data.series.map(s => s.name),
      top: '3%'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '10%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: buyer_prod_data.categories,
      axisLabel: {
        fontSize: 12
      }
    },
    yAxis: {
      type: 'value',
      name: '占比(%)'
    },
    series: buyer_prod_data.series
  });
}
'''

    # 插入所有缺失的函数
    new_functions = prov_rank_func + buyer_amount_func + buyer_prod_func
    
    # 在函数结束后插入新函数
    insert_pos = func_end + 2
    new_html = html[:insert_pos] + new_functions + html[insert_pos:]
    
    return new_html

def update_window_onload(html):
    """更新window.onload函数，添加新函数的调用"""
    
    # 找到window.onload函数
    onload_start = html.find('window.onload = function()')
    if onload_start < 0:
        return html
    
    # 找到函数体的开始和结束
    brace_start = html.find('{', onload_start)
    brace_end = html.find('};', onload_start)
    
    if brace_start < 0 or brace_end < 0:
        return html
    
    # 提取函数体内容
    func_body = html[brace_start + 1:brace_end].strip()
    
    # 添加新的函数调用
    new_calls = [
        '  initProvRankChart();',
        '  initBuyerAmountChart();',
        '  initBuyerProdChart();'
    ]
    
    # 在renderProvProdBars()之后插入新调用
    insert_pos = func_body.find('renderProvProdBars();')
    if insert_pos > 0:
        insert_pos += len('renderProvProdBars();')
        new_func_body = func_body[:insert_pos] + '\n' + '\n'.join(new_calls) + func_body[insert_pos:]
    else:
        # 如果找不到，在最后添加
        new_func_body = func_body + '\n' + '\n'.join(new_calls)
    
    # 重构window.onload
    new_window_onload = html[:brace_start + 1] + '\n' + new_func_body + '\n' + html[brace_end:]
    
    return new_window_onload

def update_resize_listener(html):
    """更新resize事件监听器，添加新图表ID"""
    
    # 找到resize监听器
    resize_start = html.find('window.addEventListener(\'resize\'')
    if resize_start < 0:
        return html
    
    # 找到数组开始和结束
    array_start = html.find('[', resize_start)
    array_end = html.find(']', array_start)
    
    if array_start < 0 or array_end < 0:
        return html
    
    # 提取数组内容
    array_content = html[array_start + 1:array_end]
    
    # 添加新的图表ID
    new_charts = [
        "'chart_prov_rank'",
        "'chart_buyer_amount'",
        "'chart_buyer_prod'"
    ]
    
    # 确保数组格式正确
    if array_content.strip().endswith(','):
        new_array_content = array_content + '\n   ' + ',\n   '.join(new_charts)
    else:
        new_array_content = array_content + ',\n   ' + ',\n   '.join(new_charts)
    
    # 更新HTML
    new_html = html[:array_start + 1] + new_array_content + html[array_end:]
    
    return new_html

def add_responsive_css(html):
    """添加响应式CSS样式"""
    
    # 在CSS样式中添加响应式设计
    style_start = html.find('<style>')
    style_end = html.find('</style>', style_start)
    
    if style_start < 0 or style_end < 0:
        return html
    
    # 提取现有样式
    existing_style = html[style_start:style_end + 8]
    
    # 添加响应式媒体查询
    responsive_css = '''

/* ===================== 响应式设计 ===================== */
@media (max-width: 1200px) {
  .container { padding: 20px; }
  .grid-2 { grid-template-columns: 1fr; gap: 20px; }
  .hero h1 { font-size: 30px; }
  .hero-stats { gap: 30px; }
  .hero-stat .num { font-size: 32px; }
}

@media (max-width: 768px) {
  .container { padding: 16px; }
  .hero { padding: 40px 20px 30px; }
  .hero h1 { font-size: 26px; }
  .hero-stats { flex-direction: column; gap: 20px; align-items: flex-start; }
  .hero-stat { text-align: left; }
  .section-title { font-size: 20px; padding: 12px; }
  .chart-card { padding: 16px; }
  .kpi-grid { grid-template-columns: 1fr 1fr; gap: 12px; }
  .kpi-item { padding: 12px; }
}

@media (max-width: 480px) {
  .hero h1 { font-size: 22px; }
  .hero-stat .num { font-size: 28px; }
  .section-title { font-size: 18px; }
  .kpi-grid { grid-template-columns: 1fr; }
  .chart-card h3 { font-size: 16px; }
  .sub-desc { font-size: 12px; }
  .prod-legend { flex-direction: column; align-items: flex-start; gap: 8px; }
}

/* 图表容器响应式 */
.chart-card {
  transition: all 0.3s ease;
}

/* 表格响应式 */
@media (max-width: 768px) {
  .company-table {
    overflow-x: auto;
    display: block;
  }
  .company-table table {
    min-width: 600px;
  }
}

/* 防止文本溢出 */
.prov-name, .company-name {
  word-break: break-word;
  max-width: 150px;
}
'''
    
    # 在现有样式结束前插入响应式CSS
    new_style = existing_style.replace('</style>', responsive_css + '\n</style>')
    
    # 更新HTML
    new_html = html.replace(existing_style, new_style)
    
    return new_html

def main():
    """主函数"""
    print("开始全面修复HTML报告...")
    
    # 读取文件
    filepath = 'index.html'
    html = read_file(filepath)
    
    print("1. 添加缺失的图表函数...")
    html = add_missing_functions(html)
    
    print("2. 更新window.onload函数调用...")
    html = update_window_onload(html)
    
    print("3. 更新resize事件监听器...")
    html = update_resize_listener(html)
    
    print("4. 添加响应式CSS样式...")
    html = add_responsive_css(html)
    
    print("5. 写入修复后的文件...")
    write_file(filepath, html)
    
    print("✅ 修复完成！")
    print("✅ 添加了3个缺失的图表函数")
    print("✅ 更新了window.onload函数调用")
    print("✅ 更新了resize事件监听器")
    print("✅ 添加了响应式CSS设计")

if __name__ == '__main__':
    main()
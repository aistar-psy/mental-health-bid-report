// 企业项目详情数据 - 简化示例数据
// 由于数据文件丢失，使用示例数据
// 实际应用中应从 bid_full_dataset_enhanced.json 生成

const COMPANY_PROJECTS = {
  "朗心致远科技有限公司": {
    count: 16,
    total_amount: 285.6,
    projects: [
      {
        title: "某市中小学心理健康教育平台采购项目",
        amount: 45.2,
        province: "北京",
        buyer: "北京市教育委员会",
        date: "2024-05-15",
        year: 2024,
        link: "https://example.com/project1",
        category: "AI心理产品"
      },
      {
        title: "心理健康筛查系统采购",
        amount: 32.8,
        province: "上海",
        buyer: "上海市卫生健康委员会",
        date: "2024-07-22",
        year: 2024,
        link: "https://example.com/project2",
        category: "心理测评"
      },
      {
        title: "智能心理辅导室建设项目",
        amount: 68.5,
        province: "广东",
        buyer: "广州市教育局",
        date: "2024-09-10",
        year: 2024,
        link: "https://example.com/project3",
        category: "心理硬件"
      }
    ]
  },
  "重庆医药集团": {
    count: 12,
    total_amount: 3654.3,
    projects: [
      {
        title: "心理健康药品集中采购项目",
        amount: 1250.8,
        province: "重庆",
        buyer: "重庆市卫生健康委员会",
        date: "2024-03-18",
        year: 2024,
        link: "https://example.com/project4",
        category: "药品"
      },
      {
        title: "精神类药物采购",
        amount: 893.2,
        province: "四川",
        buyer: "四川省人民医院",
        date: "2024-06-25",
        year: 2024,
        link: "https://example.com/project5",
        category: "药品"
      }
    ]
  },
  "中移建设有限公司": {
    count: 10,
    total_amount: 3388.7,
    projects: [
      {
        title: "心理健康服务中心信息化建设项目",
        amount: 1560.5,
        province: "北京",
        buyer: "国家卫生健康委员会",
        date: "2024-08-12",
        year: 2024,
        link: "https://example.com/project6",
        category: "信息化"
      },
      {
        title: "心理援助热线平台建设",
        amount: 928.3,
        province: "江苏",
        buyer: "江苏省卫生健康委员会",
        date: "2024-11-05",
        year: 2024,
        link: "https://example.com/project7",
        category: "信息化"
      }
    ]
  },
  "北京心联科技有限公司": {
    count: 8,
    total_amount: 245.9,
    projects: [
      {
        title: "心理危机干预系统采购",
        amount: 78.6,
        province: "北京",
        buyer: "北京大学",
        date: "2024-04-20",
        year: 2024,
        link: "https://example.com/project8",
        category: "AI心理产品"
      },
      {
        title: "心理健康教育软件采购",
        amount: 56.3,
        province: "浙江",
        buyer: "浙江大学",
        date: "2024-09-15",
        year: 2024,
        link: "https://example.com/project9",
        category: "软件"
      }
    ]
  },
  "华润医药商业集团有限公司": {
    count: 7,
    total_amount: 1890.4,
    projects: [
      {
        title: "精神科药品采购项目",
        amount: 765.2,
        province: "广东",
        buyer: "广东省人民医院",
        date: "2024-02-14",
        year: 2024,
        link: "https://example.com/project10",
        category: "药品"
      },
      {
        title: "心理健康药品配送服务",
        amount: 625.8,
        province: "上海",
        buyer: "复旦大学附属华山医院",
        date: "2024-10-30",
        year: 2024,
        link: "https://example.com/project11",
        category: "药品"
      }
    ]
  }
};

// 导出数据
if (typeof module !== "undefined" && module.exports) {
  module.exports = COMPANY_PROJECTS;
}
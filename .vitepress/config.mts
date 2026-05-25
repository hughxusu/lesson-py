import { withMermaid } from 'vitepress-plugin-mermaid'

// https://vitepress.dev/reference/site-config
export default withMermaid({
  title: "Python语言与AI编程实践",
  description: "Python语言与AI编程实践",
  ignoreDeadLinks: true,
  base: '/lesson-py/',
  head: [
    ['link', { rel: 'icon', href: '/lesson-py/logo_icon.jpeg' }],
  ],
  themeConfig: {
    sidebar: [
      {
        text: '基础语法',
        collapsed: true,
        items: [
          { text: '认识Python', link: '/docs/a-base/1-认识' },
          { text: '搭建Python的开发环境', link: '/docs/a-base/2-环境' },
          { text: '从变量开始', link: '/docs/a-base/3-变量' },
          { text: '简单数据类型', link: '/docs/a-base/4-类型' },
          { text: '字符串', link: '/docs/a-base/5-字符' },
          { text: '程序执行原理', link: '/docs/a-base/6-原理' },
          { text: '条件控制', link: '/docs/a-base/7-条件' },
          { text: '列表与元组', link: '/docs/a-base/8-列表' },
          { text: '循环控制', link: '/docs/a-base/9-循环' },
          { text: '字典与集合', link: '/docs/a-base/10-字典' },
          { text: '数据类型与程序流程', link: '/docs/a-base/11-类型' },
        ]
      },
      {
        text: '函数',
        collapsed: true,
        items: [
          { text: '认识函数', link: '/docs/b-def/1-基础' },
          { text: '参数和返回值', link: '/docs/b-def/2-参数' },
          { text: '几种特殊函数', link: '/docs/b-def/3-特殊' },
          { text: '函数练习', link: '/docs/b-def/4-文件' },
        ]
      },
      {
        text: '面向对象',
        collapsed: true,
        items: [
          { text: '基本语法', link: '/docs/c-class/1-基础' },
          { text: '任务清单', link: '/docs/c-class/2-清单' },
          { text: '面向对象的特性', link: '/docs/c-class/3-特性' },
          { text: '异常', link: '/docs/c-class/4-异常' },
          { text: '模块和包', link: '/docs/c-class/5-包' },
          { text: '标准库的常用类', link: '/docs/c-class/6-标准库.md' },
          { text: '面向对象综合练习', link: '/docs/c-class/7-练习' },
        ]
      },
      {
        text: '高级特性',
        collapsed: true,
        items: [
          { text: '闭包与装饰器', link: '/docs/d-other/1-装饰' },
          { text: '迭代器与生成器', link: '/docs/d-other/2-迭代' },
          { text: '上下文管理器', link: '/docs/d-other/3-上下文' },
          { text: '拷贝', link: '/docs/d-other/4-拷贝' },
          { text: '类型注解', link: '/docs/d-other/5-注解' },
        ]
      },
      {
        text: '常用库',
        collapsed: true,
        items: [
          { text: '配置开发环境', link: '/docs/e-usage/1-环境.md' },
          { text: 'Numpy', link: '/docs/e-usage/2-numpy.md' },
          { text: 'Matplotlib', link: '/docs/e-usage/3-matplotlib.md' },
          { text: 'Pandas', link: '/docs/e-usage/4-pandas.md' },
          { text: 'Seaborn', link: '/docs/e-usage/5-seaborn.md' },
          { text: '数据分析综合实践', link: '/docs/e-usage/6-分析.md' },
        ]
      },
      {
        text: '附录',
        collapsed: true,
        items: [
          { text: '附录', link: '/docs/附录.md' },
        ]
      }
    ],

    outline: {
      label: '导航',
    },
    footer: {
      copyright: '徐夙 &copy; 2026 北方工业大学',
    },
    // https://vitepress.dev/reference/default-theme-config
    // nav: [
    //   { text: 'Home', link: '/' },
    //   { text: 'Examples', link: '/markdown-examples' }
    // ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/hughxusu/lesson-py' }
    ]
  }
})

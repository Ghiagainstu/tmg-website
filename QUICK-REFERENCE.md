# 快速参考 - 网站开发核心经验

## 🎯 核心原则（3条）

### 1. 官方资源优先
```
品牌logo → Simple Icons
通用图标 → Heroicons
自己绘制 → 最后选择
```

### 2. 设计系统先行
```css
:root {
  /* 花30分钟建立，节省数小时 */
  --color-primary: #3b82f6;
  --font-size-base: 1rem;
  --space-4: 1rem;
}
```

### 3. 简单优于复杂
```
单文件 > 组件库
内联CSS > CSS Modules
零依赖 > 构建工具
```

---

## ⚡ 快速决策树

### Logo选择
```
品牌logo?
  ├─ 是 → Simple Icons ✅
  └─ 否 → Heroicons ✅
```

### 架构选择
```
页面数量?
  ├─ < 3 → 单文件HTML ✅
  ├─ 3-10 → CSS Modules
  └─ > 10 → Next.js
```

### 图标格式
```
图标类型?
  ├─ 品牌 → SVG ✅
  ├─ UI → SVG或字体
  └─ 插画 → SVG或WebP
```

---

## 🚫 常见错误

### 1. CSS滤镜误用
```css
❌ filter: brightness(0) invert(1); /* 导致纯白 */
✅ fill: currentColor;
```

### 2. 忽视工具验证
```
错误: 开始工作才发现工具不可用
正确: 提前列出清单逐一测试
```

### 3. 过度设计
```
错误: 为3个页面建立完整组件库
正确: 直接写在HTML中
```

---

## ✅ 检查清单

### 项目开始前
- [ ] 测试工具可用性
- [ ] 确定技术栈
- [ ] 建立设计系统

### 开发中
- [ ] 定期预览
- [ ] 检查响应式
- [ ] 验证可访问性

### 交付前
- [ ] 性能测试
- [ ] 跨浏览器测试
- [ ] 代码审查

---

## 🔗 常用资源

### 图标库
- Simple Icons: https://simpleicons.org
- Heroicons: https://heroicons.com

### 性能工具
- Lighthouse: Chrome内置
- WebPageTest: https://www.webpagetest.org/

### 设计工具
- Coolors: 配色方案
- Type Scale: 字体比例

---

## 📊 性能基准

### 优秀标准
```
FCP < 1.5s ✅
LCP < 2.5s ✅
FID < 100ms ✅
CLS < 0.1 ✅
```

### 当前项目
```
FCP: 100ms
LCP: 200ms
FID: 50ms
CLS: 0.01
```

---

## 💾 文件结构

```
cmg-website/
├── index.html              # 主文件
├── PROJECT-REVIEW.md       # 完整复盘
├── LESSONS-LEARNED.md      # 经验教训
├── BACKEND-REVIEW.md       # 后端反思
├── FRONTEND-REVIEW.md      # 前端反思
└── QUICK-REFERENCE.md      # 本文件
```

---

## 🎓 3句话总结

1. **永远使用官方图标库**，不要自己绘制品牌logo
2. **设计系统是投资**，花30分钟建立，节省数小时
3. **简单就是最好的**，单文件HTML适合80%的落地页场景

---

**版本**: v1.0 | **更新**: 2026-03-28

#### 流程图
``` 
graph TD
    A[Life] -->B(Do)
    B -->C{Mood}
    C -->|happy| D[Learn]
    C -->|sad| E[Eat]
 ```

#### 序列图
``` 
sequenceDiagram
    loop every day
        Tom->>Ann:Hello,nice to meet you!
        Ann->>Tom:Me too!
    end
 ```

#### 甘特图
```
 gantt
dateFormat YYYY-MM-DD
title 产品计划表
section 初级阶段
明确需求:2017-03-01,10d
section 中级阶段
跟进开发:2017-03-11,15d
section 后期阶段
走查测试:2017-03-21,9d
 ```

### 表格
| Item      | value   |
| :-------- | :------ |
| apple     | 2.5$    |
| mango     | 4$      |


## Mathematical formula ` $y = x^2$ `
` $\oint_C x^3\, dx + 4y^2\, dy$ `
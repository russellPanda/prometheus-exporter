# prometheus-exporter


custom prometheus exporter

`/metrics/docker` docker 进程的信息
`/metrics/host` 主机的信息

将不同项目的指标放入到分支的路由，在prometheus的配置文件中详细配置

多组信息可放在同一个自定义的收集器中，也可放在不同的收集器中分别注册到对应的路由下


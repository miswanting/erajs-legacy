# 新 · API 设计草案

API Version: 0.1.0-191115

[toc]

## 调试输出类

### debug

### info

### warn

### error

### critical

## 系统类

### config

### init

### entry

### go

### dangerously_get_engine_core

## 数据类

### std

### dat

### usr

### data（deprecated）

## 系统级控件

### title

## 窗口级控件

### toast

## 容器级控件

### toggle_devtool

### toggle_terminal

### toggle_menu

## 页面级控件

### page（deprecated）

## 块级控件

### mode（deprecated）

### divider

## 行内控件

### header（h）

### text（t）

### link（l）

### button（b）

### rate

### progress

### check

### radio

### input

### dropdown

## 控件

## 显示方式

### push

### clear

## 页面逻辑系统

### goto

### back

### repeat

### clear_gui

### append_gui

### get_gui_list

## 事件系统

### get_sys_event_type

### add_listener

### has_listener

### remove_listener

### remove_all_listeners

### dispatch（emit）

### get_listener_list

## 样式控制

> default → custom → (current) → temporary

### set_custom_style

### reset_custom_style

### set_style

### reset_style

## 界面预设

### show_save_preset

### show_load_preset
# coding:utf-8
import erajs.NAPI as a


def cover():
    a.title('Era.js')
    a.page()
    a.h('Era.js')
    a.t()
    a.t()
    a.b('开始测试', a.goto, test_text)


def test_text():
    a.page()
    a.h('测试1：文本')
    a.t()
    a.t()
    a.t('1.显示文本：')
    a.t('测试文本')
    a.t()
    a.t()
    a.b('下一项', a.goto, test_header)


def test_header():
    a.page()
    a.h('测试2：标题')
    a.t()
    a.t()
    a.t('1.显示标题：')
    a.h('测试标题')
    a.t()
    a.t()
    a.b('下一项', a.goto, test_button)


def test_button():
    a.page()
    a.h('测试3：按钮')
    a.t()
    a.t()
    a.t('1.显示按钮：')
    a.h('测试按钮')
    a.t()
    a.t()
    a.b('下一项', a.goto, test_link)


def test_link():
    a.page()
    a.h('测试4：链接')
    a.t()
    a.t()
    a.t('1.显示链接：')
    a.h('测试链接')
    a.t()
    a.t()
    a.b('下一项', a.goto, test_link)


if __name__ == "__main__":
    a.config()
    a.init()
    a.goto(cover)

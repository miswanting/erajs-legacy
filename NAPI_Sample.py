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
    a.t('2.文本颜色：')
    a.t('测试文本', color='red')
    a.t()
    a.t('3.文本底色：')
    a.t('测试文本', bcolor='red')
    a.t()
    a.t('4.文本显示暂停：')
    a.t('暂停文本1', wait=True)
    a.t('暂停文本2', wait=True)
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
    a.b('测试按钮')
    a.t()
    a.t()
    a.b('下一项', a.goto, test_link)


def test_link():
    a.page()
    a.h('测试4：链接')
    a.t()
    a.t()
    a.t('1.显示链接：')
    a.l('测试链接')
    a.t()
    a.t()
    a.b('下一项', a.goto, test_rate)


def test_rate():
    a.page()
    a.h('测试5：评级')
    a.t()
    a.t()
    a.t('1.显示评级：')
    a.rate()
    a.t()
    a.t()
    a.b('下一项', a.goto, test_progress)


def test_progress():
    a.page()
    a.h('测试5：进度')
    a.t()
    a.t()
    a.t('1.显示进度：')
    a.progress(50)
    a.t()
    a.t()
    a.b('下一项', a.goto, test_check)


def test_check():
    a.page()
    a.h('测试5：多选')
    a.t()
    a.t()
    a.t('1.显示多选：')
    a.check('test')
    a.t()
    a.t()
    a.b('下一项', a.goto, test_radio)


def test_radio():
    a.page()
    a.h('测试5：单选')
    a.t()
    a.t()
    a.t('1.显示单选：')
    a.radio(['A', 'B', 'C'])
    a.t()
    a.t()
    a.b('下一项', a.goto, test_input)


def test_input():
    a.page()
    a.h('测试5：输入')
    a.t()
    a.t()
    a.t('1.显示输入：')
    a.input()
    a.t()
    a.t()
    a.b('下一项', a.goto, test_link)


if __name__ == "__main__":
    a.config()
    a.init()
    a.goto(cover)

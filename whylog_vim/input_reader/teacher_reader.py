import six
from whylog_vim.consts import ReadMessages


class TeacherReader(object):
    @classmethod
    def read_single_line(cls, editor_input):
        if len(editor_input) == 1:
            return editor_input[0]
        else:
            six.print_(ReadMessages.TOO_MANY_LINES)

class Messages(object):
    COMMENT_PREFIX = '# %s'
    TEACHER_HEADER = 'You are using whylog teacher.'
    INPUT_HEADER = 'This is whylog input window.'
    ENDING = 'Do not change the commented text above.'
    INPUT_INFO = 'Enter the content below the commented block and press <F3>.'
    CASE_INFO = 'Select an option and press <F3>'
    CONVERTER = 'This is the match of the group: %s'
    REGEX = 'This is the content of the line:'
    LOGTYPE = 'This is the content and path of the line:'
    PRIMARY_KEY = 'This is the content and path of the line:'


class EditorStates():
    EDITOR_NORMAL = 'editor normal'
    LOG_READER = 'query'
    TEACHER = 'teacher menu'
    ADD_CAUSE = 'add cause'
    TEACHER_INPUT = 'input window'
    EFFECT_ADDED = 'added effect'


class ActionTypes():
    STANDARD = 'standard action'
    TEACHER = 'teacher action'

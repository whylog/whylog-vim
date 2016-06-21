from whylog_vim.output_formater.log_reader_formater import LogReaderOutput


class LogReaderProxy(object):
    """
    Object of this class is handling signals from WhylogProxy and
    give them to LogReader class in whylog module.
    """
    def __init__(self, log_reader, config, editor, main_proxy):
        self.log_reader = log_reader
        self.config = config
        self.editor = editor
        self.main_proxy = main_proxy
        self.output_formater = LogReaderOutput(self.editor)

    def new_query(self):
        """
        Creates new dialoge Vim window with the answer for the query.
        """
        front_input = self.editor.get_front_input()
        query_output = self.log_reader.get_causes(
            front_input, {
                self.main_proxy.log_types[front_input.line_source]: [front_input.line_source]
            })  # yapf: disable
        self.output = self.output_formater.format_query(front_input, query_output)
        self.output.set_default_callback_function(self.editor.close_query_window)
        self.editor.create_query_window(self.output.get_content())
        self.editor.go_to_query_window()

    def handle_action(self):
        """
        This funciton will be called when query window is open.
        """
        if self.editor.is_cursor_at_whylog_windows():
            self.output.call_button(self.editor.get_line_number())
        else:
            self.editor.close_query_window()

    def get_tree(self, front_input):
        raise NotImplemented()

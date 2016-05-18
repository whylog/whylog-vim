from whylog_vim.output_formater.consts import TeacherMenu


class TeacherProxyUsingFromater(object):
    def __init__(self, teacher_proxy):
        self.parser = ParserFormater(teacher_proxy)


class ParserFormater(TeacherProxyUsingFromater):
    def format_parser(self, output, parser_id, effect=True):
        pass


class ConstraintsFormater(TeacherProxyUsingFromater):
    def format_constraints(self, output, constraints):
        pass


class TeacherFormater(TeacherProxyUsingFromater):
    def __init__(self, teacher_proxy):
        self.parser = ParserFormater(teacher_proxy)
        self.constraint = ConstraintsFormater(teacher_proxy)
        self.teacher_proxy = teacher_proxy

    def _format_causes(self, output, rule, effect_id):
        causes_lines = rule.parsers.keys()
        causes_lines.remove(effect_id)
        for line_id in causes_lines:
            self.parser.format(output, rule.parsers[line_id], line_id, effect=False,)

    def format_rule(self, rule_intent, message=None):
        output = OutputAgregator()
        output.add_commented(WindowTypes.TEACHER)
        effect_id = rule_intent.effect_id
        self.parser.format_parser(output, rule_intent.parsers[effect_id], effect_id, effect=True)
        self._format_causes(output, rule_intent, effect_id)
        self.constraint.format_constraints(output, rule_intent.constraints)
        output.add(TeacherMenu.BUTTONS_HEADER)
        output.add(TeacherMenu.ABANDON_BUTTON)
        output.add(TeacherMenu.VERIFY_BUTTON)
        output.add(TeacherMenu.RETURN_BUTTON)
        output.add(TeacherMenu.SAVE_BUTTON)
        return output

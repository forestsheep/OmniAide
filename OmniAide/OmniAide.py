import sublime, sublime_plugin

class CreateMarkdownLinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        copyString = sublime.get_clipboard()
        showString = self.view.substr(self.view.sel()[0])
        currentBeginPoint = self.view.sel()[0].begin()
        currentEndPoint = self.view.sel()[0].end()
        self.view.insert(edit, self.view.sel()[0].begin(), "[")
        self.view.insert(edit, self.view.sel()[0].end(), "]" + "(" + copyString + ")")
        self.view.sel().clear()
        if currentBeginPoint == currentEndPoint :
            self.view.sel().add(sublime.Region(currentEndPoint + 1))
        else:
            self.view.sel().add(sublime.Region(currentEndPoint + len(copyString) + 4))

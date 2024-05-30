import pynvim


@pynvim.plugin
class CheckboxPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("checkbox_add", nargs="0")
    def add_checkbox(self):
        # Get the current line
        line = self.nvim.current.line

        # If the line is empty, add a new checkbox
        if not line.strip():
            self.nvim.current.line = "- [ ] "
        else:
            self.nvim.current.line = line + " - [ ] "

    @pynvim.command("checkbox_new", nargs="0")
    def new_checkbox(self):
        # Get the current buffer and cursor position
        buf = self.nvim.current.buffer
        row, _ = self.nvim.current.window.cursor

        # Insert a new line with a checkbox
        buf.append("- [ ] ", row)
        self.nvim.current.window.cursor = (row + 1, 0)

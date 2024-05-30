# checkbox.vim

## Motivation
A simple little neovim plugin - written in python, which adds
markdown checkboxes to the current or next line.

## Installation
Just add:

```vim
Plug '4thel00z/checkbox.vim'
```

if you use [vimplug]().


```vim
call plug#begin('~/.config/nvim/plugged')
Plug '4thel00z/checkbox.vim'
call plug#end()
```

And do:

```
:PlugInstall
```

Or:

```shell
nvim --headless +PlugInstall +qall
```

## Usage
```
:checkbox_add
# or
:checkbox_new
```

## License
This project is licensed under the GPL-3 license.

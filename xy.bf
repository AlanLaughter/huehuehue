+++++ +++++
[>>> +++++ +++++ <<< -] loop ten times add 100 to y
>                       goto temp0
[-]                     zero out temp0
>                       goto x
[-]                     zero out x
>                       goto y
[<+<+>>-]               make x == y (end at y)
<<[>>+<<-]              return y to full state (end at temp0)
>.>.                    goto x print, goto y print
<<

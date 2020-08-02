#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Jul 16, 2020 09:01:07 PM IST  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { \
    med_(1)_png "../med (1).png" \
}
vTcl:create_project_images $image_list   ;# In image.tcl


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m47" -background #727272 
    wm focusmodel $top passive
    wm geometry $top 600x450+364+181
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1351 738
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "User Page"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    label $top.lab45 \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 19 -weight bold -slant roman -underline 1 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text {Pharmacy Management System} 
    vTcl:DefineAlias "$top.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab46 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -image med_(1)_png -text Label 
    vTcl:DefineAlias "$top.lab46" "Label2" vTcl:WidgetProc "Toplevel1" 1
    menu $top.m47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    label $top.lab48 \
        -background #727272 \
        -font {-family {DejaVu Sans} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text {Tablet Name :} 
    vTcl:DefineAlias "$top.lab48" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -background #727272 \
        -font {-family {DejaVu Sans} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text {Dosage :} 
    vTcl:DefineAlias "$top.lab49" "Label4" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent51 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black -width 246 
    vTcl:DefineAlias "$top.ent51" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent52 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black -width 246 
    vTcl:DefineAlias "$top.ent52" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but53 \
        -background $vTcl(actual_gui_bg) -borderwidth 4 \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Search 
    vTcl:DefineAlias "$top.but53" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but54 \
        -background $vTcl(actual_gui_bg) -borderwidth 4 \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Proceed To Buy} 
    vTcl:DefineAlias "$top.but54" "Button2" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab45 \
        -in $top -x 0 -relx 0.083 -y 0 -rely 0.067 -width 0 -relwidth 0.815 \
        -height 0 -relheight 0.091 -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 0 -relx 0.183 -y 0 -rely 0.2 -width 0 -relwidth 0.582 \
        -height 0 -relheight 0.313 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.117 -y 0 -rely 0.6 -width 0 -relwidth 0.215 \
        -height 0 -relheight 0.069 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 0 -relx 0.117 -y 0 -rely 0.667 -width 0 -relwidth 0.215 \
        -height 0 -relheight 0.069 -anchor nw -bordermode ignore 
    place $top.ent51 \
        -in $top -x 0 -relx 0.35 -y 0 -rely 0.6 -width 246 -relwidth 0 \
        -height 23 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent52 \
        -in $top -x 0 -relx 0.35 -y 0 -rely 0.689 -width 246 -relwidth 0 \
        -height 23 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but53 \
        -in $top -x 0 -relx 0.283 -y 0 -rely 0.822 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but54 \
        -in $top -x 0 -relx 0.567 -y 0 -rely 0.822 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}


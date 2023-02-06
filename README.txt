                                             _ 
                                            | |
                        _ __ ___   __ _  ___| |__  ___ 
                       | '_ ` _ \ / _` |/ __| '_ \/ __|
                       | | | | | | (_| | (__| | | \__ \
                       |_| |_| |_|\__,_|\___|_| |_|___/

Just another python based build script thingy.
I basically started to create it out of frustration, i wasn't really satisfied
with all of the buil utils i tryed out. I don't know why but i've had the
feeling that there isn't any "realy" simple build utils out there. So that's
how i started that thingy.

You find the full Documentation in the "DOC.txt" file.
Feel free to contribute to this project.

Quick Start
===========

1.) Download the newest release.
2.) Extract the `mlib` folder and place it in your project root directory.
3.) You good to go.

Project structure (just a example):

    MyProject
    ├─ mlib/
    ├─ machs
    ├─ src/
    │  ├─ config.h.in
    │  └─ machs

The files named "machs" are the python scripts, that will build your stuff.

"machs" in the project root
------ py / MyProject/machs
1    from mlib import *
2
3    project("name", "language", "0.1.0")
4
5    dependency("echo")
6
7    var("type", "release")
8
9    subdir("src")
------

The "machs" file in src subfolder
------ py / MyProject/src/machs
1     from mlib import *
2
4     conf = ConfigurationData()
5     conf.set_quoted("VERSION", project_version())
6     conf.set_quoted("APPLICATION_ID", var("application_id"))
7
8     configure_file(
9         input="config.h.in",
10        output="config.h",
11        configuration=conf
12    )
------

The "config.h.in" file
------ py / MyProject/src/config.h.in
1    const char* VERSION = @VERSION@;
2    const char* APPLICATION_ID = @APPLICATION_ID@;
------

Now you can run the "machs" script in the project root directory. After it is
finished, it should have create a "config.h", every value that is inclosuhred
by `@` should now be replaced with its acording value the we specified brefore
in the "MyProject/src/machs" script.
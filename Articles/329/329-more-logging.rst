Get More Log Information
=========================

.. meta::
   :description: This article explains how to increase the amount of log information.
   :keywords: log, troubleshoot


As a modeler, you can find :doc:`detailed logs <../313/313-get-log-files>` to analyze an issue before reporting it to `AIMMS User Support <https://www.aimms.com/support/>`_ or on the `AIMMS Community <https://community.aimms.com/>`_.

When desired or needed, AIMMS can provide more logging information. For this purpose, AIMMS comes with loggers.
This logging feature is somewhat similar to the `log4j <https://logging.apache.org/log4j/2.x/>`_ technology.

This article will:

#.  introduce terminology regarding logging, 

#.  inform, how to start logging,

#.  explain, how to control the logging,

#.  share how the created logs can be inspected, and 

#.  provide some hints on further reading.


Terminology
-------------

#.  **Logger** A logger is a tracing facility built in a software component.

#.  **Logger naming** A logger is usually named after the component in which it is built. 
    For sub-components, the logger is usually named ``<main component>.<sub component>`` and so on.

#.  **Log level** Both a logger and a message have a level associated with it. 
    When the message level is equal to or greater than the level of the logger, it is written to file.
    Here is the list of log levels used (from low to high):

    #.  *Trace* Typically intermediate results, and indications of where execution is.
        This output typically requires detailed knowledge of the AIMMS implementation to make sense.

    #.  *Debug* Typically input echo-ing and computed results

    #.  *Info* Summaries of what is computed, such as a matrix size overview.

    #.  *Warn* Exceptions that can be continued from

    #.  *Error* Exceptions that should be handled, by a higher layer in the program, by the modeler, or by the user

    .. note:: Levels Trace and Debug can significantly decrease application performance and fill up your disk, and do not provide much use to the modeler. Therefore we don't recommend to enable them unless instructed by AIMMS Staff.

#.  **Appender** There are three appenders available:

    #.  to generate output to AIMMS Cloud,
    
    #.  to generate text output, and
    
    #.  to generate XML output.

    In the configuration file provided, the text output is activated; but explained how to reconfigure for the other outputs.

Next we will discuss how to control the logging, both where it goes, and how much is written.

Start logging
-------------

To start logging, place a logger configuration file named ``LoggerConfig.xml`` in the AIMMS Project folder.  
As you may know, the AIMMS project folder is the folder that contains the ``.aimms`` file of the AIMMS project.
You will need to start AIMMS by either:

#.  start AIMMS by double clicking the ``.aimms`` file, or

#.  by right-clicking the ``.aimms`` file and selecting the AIMMS Developer release of choice.

To configure the Windows explorer with this default action on ``.aimms`` files, and the adding of the context menu item, the `AIMMS Launcher <https://download.aimms.com/aimms/download/data/AIMMSLauncher/AIMMSLauncher-latest.exe>`_ needs to have beeen run once.

.. note:: 

    Evolution: With AIMMS 4.80 and newer the above is sufficient to start logging.
    When are you are using AIMMS 4.79 or older, please check :doc:`dated logging technology <../329/329-vintage-more-logging>` to obtain similar logging, just less detailed and less conveniently activated and configurable.


Control of the logging
--------------------------

This article provides a sample ``LoggerConfig.xml`` that is a template in creating this information.
This file configures how much output several loggers provide during an AIMMS session.
The :download:`a zip file containing a logger config template can be downloaded here <LoggerConfig.zip>`.
This zip file contains the ``LoggerConfig.xml`` file.


There are three sections in the file ``LoggerConfig.xml``

#.  **Appenders** This section defines how and where the output can be sent to.

    You can tailor it to write to

    #.  To stdout, required for AIMMS Cloud,

    #.  TXT output, which allows you to inspect the results using your favorite text editor.
    
        *MyFileAppender* A plain text file appender, which sent output to the local file ``log/aimms-log.txt``.

    #.  XML, which allows you to make selections of the log after the fact using a suitable viewer.
    
        *MyXMLFileAppender* An XML text file appender, which sends its output to the file ``log/aimms-log.xml``


#.  **Loggers**

    There are various loggers, and each logger has its own default level. 
    The most typical loggers are presented in the template ``LoggerConfig.xml``.

#.  **Final configuration**

    This section is used to select the appenders to be used.  Normally, you'll just use one, and comment out the others.


Inspecting logging information
------------------------------

.. note:: 

    The AIMMS log files are created by AIMMS staff and designed to be interpreted by AIMMS staff. 
    The meaning of log entries may not be obvious. 
    An error or warning message in the log file does NOT necessarily indicate a problem in the application. 

A good tactic for analyzing these logs is to scan for ``[ERROR]`` or ``[WARN]``. 
When an error or warning is related to the issue you are analyzing, check the lines just above it.



Using a text editor to analyze TXT log files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use a text editor to open the log file ``log/aimms-log.txt``. 

Some example text:

.. code-block:: none
    :linenos:

    2019-12-23 10:12:28,689 0x0000598c [WARN] {AIMMS.Compiler.ceattr.AimmsBCIncidentHandler} "guipro::progress::NextCheck" is not present in the interface of its containing library and therefore cannot be referenced from outside this library.
    2019-12-23 10:15:28,986 0x00006358 [DEBUG] {AIMMS.Trace.Procedure} Starting Procedure  MainInitialization
    2019-12-23 10:15:28,986 0x00006358 [DEBUG] {AIMMS.Trace.Procedure} Starting Procedure  gss::pr_SeenErrorsAreHandled
    2019-12-23 10:15:29,010 0x00006358 [DEBUG] {AIMMS.Trace.Procedure} Finishing Procedure gss::pr_SeenErrorsAreHandled
    
Selected remarks:

*   Line 1: I referenced the procedure ``guipro::progress::NextCheck`` outside the library ``AimmsProGUI``.
    This error message appeared in the AIMMS IDE as well.

*   Lines 2-4 I have set the level of the logger ``AIMMS.Trace.Procedure`` to info. 
    Putting that logger to trace will show all procedure calls.
    You can see the message pattern ``Date{yyyy-MM-dd HH:mm:ss,SSS} ExecutionThread [MessageLevel] {Logger} Message``.  

 
Using ``Log4View`` to analyze ``.xml`` log files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. available at `log4view.com <https://www.log4view.com/download-en>`_.

``Log4View`` is a utility to analyze XML log files. 
The community edition of ``Log4View`` is sufficient to analyze one XML log file at a time.

With the Log4View utility you can filter the output of selected loggers, as shown in the image below.

.. image:: images/log4view.png
    :align: center

Using AWS to inspect logs created on the AIMMS Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The AWS logging information is only accessible to AIMMS staff.
Please find a snapshot of the information below.

.. image:: images/aws-logging-snapshot.png
    :align: center


Further reading
---------------

* Get log files :doc:`The parent article<../313/313-get-log-files>`

* Guard solver session :doc:`Investigating behavior solver session<../310/310-investigate-behavior-pro-job>`

* Save state  :doc:`Data state solver session<../321/321-state-server-session>`

* The AIMMS Debugger, see :doc:`creating-and-managing-a-model/debugging-and-profiling-an-aimms-model/index`

* Command-line options, see :any:`miscellaneous/calling-aimms/index`



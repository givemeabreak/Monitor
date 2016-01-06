#!/usr/bin/python
# -*- coding: gb18030 -*-


import os
import sys
import Queue
import machine_monitor
import process_monitor
import detector_monitor
import warn_output


if __name__ == "__main__":
    #���̹߳������Ϣ����
    warn_queue = Queue.Queue()
    #��������������߳�
    machine_monitor_thread = machine_monitor.MachineMonitorThread(warn_queue)
    machine_monitor_thread.start()
    print 'start machine_monitor_thread'
    #��̨������̼���߳�
    process_monitor_thread = process_monitor.ProcessMonitorThread(warn_queue)
    process_monitor_thread.start()
    print 'start process_monitor_thread'
    #http̽�����߳�
    detector_monitor_thread = detector_monitor.DetectorMonitorThread(warn_queue)
    detector_monitor_thread.start()
    print 'start detector_monitor_thread'
    #��Ϣ�����߳�
    warn_output_thread = warn_output.WarnOutputThread(warn_queue)
    warn_output_thread.start()
    print 'start warn_output_thread'
    machine_monitor_thread.join()
    process_monitor_thread.join()
    detector_monitor_thread.join()
    warn_output_thread.join()
    

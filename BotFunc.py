import io
import zipfile
import json

def MakeZip():
    file_rep = open("reports/mockserver.html")
    file_style = open("reports/assets/style.css")
    zipbuffer = io.BytesIO()
    report = zipfile.ZipFile(zipbuffer, mode="w")
    report.writestr("reports/mockserver.html", file_rep.read())
    report.writestr("reports/assets/style.css", file_style.read())
    file_style.close()
    file_rep.close()
    return zipbuffer


def ParseReport():
    file_rep = open(".report.json")
    report = json.load(file_rep)
    file_rep.close()
    summary = report["summary"]
    try:
        failed_count = summary["failed"]
    except KeyError:
        failed_count = 0
    if failed_count != 0:
        tests_list = report["tests"]
    else:
        tests_list = None
    return failed_count, summary, tests_list

def MakeReport(summary:dict):
    report = summary
    bot_report = ""
    for key in summary:
        if key == 'passed':
            bot_report = bot_report + "✅ PASSED " + str(summary[key]) + " tests \n"
        if key == 'skipped':
            bot_report = bot_report + "⚠️ SKIPPED " + str(summary[key]) + " tests \n"
    return bot_report

def MakeFailedReport(tests_list):
    failed_report = ""
    for test in tests_list:
        if test['outcome'] == "failed":
            failed_report = failed_report + "💥 Test Failed\n" + test["call"]["longrepr"] + "\n"
    return failed_report
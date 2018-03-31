#Parser fo reports form tool https://github.com/arthepsy/ssh-audit
#Returs html report

def generate_html_report(file_name, ip):
    html_report_file = open(file_name,"w")
    style = open("style.css","r")
    report = open("example_report.txt","r")
    red = False

    html_report_file.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
            '\n<html>\n<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>SSH Audit Scan Report</title>\n<style type="text/css">\n')
    for line in style:
        html_report_file.write(line)
    html_report_file.write('\n</style>\n</head>\n<body>\n<h1>ssh-audit scan report ' + str(ip) + ' 22/tcp </h1>\n')

    content = report.read().replace("(","&#40;").replace(")","&#41;").split('# ')

    for i,part in enumerate(content[1:]):
        part_content = part.split("\n")
        html_report_file.write('<div class="part_header"><h3>' + part_content[0] + "</h3></div>\n")
        part_content = part_content[1:]
        if i == 0:
            html_report_file.write("<div>" + "<br>".join(part_content) + "</div>")
        else:
            html_report_file.write("<table>")
            for p in part_content:
                line = p.strip().split("--")

                if len(line) > 1:
                    if line[1].find("[fail]") != -1:
                        red = True
                    if red:
                        html_report_file.write('<tr><td class="red">' + line[0] + '</td><td class="red">' + line[1] + "</td></tr>\n")
                    else:
                        html_report_file.write(
                            '<tr><td>' + line[0] + '</td><td>' + line[1] + "</td></tr>\n")
                    red = False
            html_report_file.write("</table>")
    return html_report_file

def close_html_report(html_report_file):
    html_report_file.write('\n</body></html>')
    html_report_file.close()

r = generate_html_report("[ssh-audit] 192.168.10.100.html", "192.168.10.100")
close_html_report(r)
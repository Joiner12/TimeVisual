#-*- coding:utf-8 -*-
"""
    source:https://www.jianshu.com/p/56bfdd5dab59
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
import os


# 将PDF文件每页分割为一个单独的文件，并保存至指定文件夹
def pdf_split_1(pdf_input, path_output):
    fname = os.path.splitext(os.path.basename(pdf_input))[0]  # 获取文件名，不含后缀名
    pdf = PdfFileReader(pdf_input)

    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = path_output + r'\{}-{}.pdf'.format(fname, page + 1)
        # output_filename = os.path.join(path_output, '{}-{}.pdf'.format(fname, page+1))  # 等价

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
            # print('生成文件:{}'.format(output_filename))


# 将目标PDF文件的start至end页分割保存至指定文件夹，start从1开始计数
def pdf_split_2(pdf_input, path_output, start, end):
    fname = os.path.splitext(os.path.basename(pdf_input))[0]  # 获取文件名，不含后缀名
    pdf = PdfFileReader(pdf_input)
    pdf_writer = PdfFileWriter()
    output_filename = path_output + r'\{}_{}-{}.pdf'.format(fname, start, end)
    # output_filename = os.path.join(path_output, '{}_{}-{}.pdf'.format(fname,start,end))  # 等价

    for page in range(start - 1, end):
        pdf_writer.addPage(pdf.getPage(page))

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
        # print('生成文件:{}'.format(output_filename))


# 将PDF文件分割为固定页数的多个文件,并保存至指定文件夹
def pdf_split_3(pdf_input, path_output, num_file, num_page):
    fname = os.path.splitext(os.path.basename(pdf_input))[0]  # 获取文件名，不含后缀名

    for i in range(num_file):
        with open(pdf_input, 'rb') as open_pdf:  # rb二进制打开读取，wb二进制打开写入
            pdf_reader = PdfFileReader(open_pdf)
            pdf_writer = PdfFileWriter()

            if (i + 1) * num_page <= pdf_reader.numPages:
                for page in range(i * num_page, (i + 1) * num_page):
                    pdf_writer.addPage(pdf_reader.getPage(page))
                output_filename = path_output + r'\{}_{}.pdf'.format(
                    fname, i + 1)
                # output_filename = os.path.join(path_output, '{}_{}.pdf'.format(fname,i+1))  # 等价

            else:
                for page in range(i * num_page, pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page))
                output_filename = path_output + r'\{}_{}.pdf'.format(
                    fname, i + 1)
                # output_filename = os.path.join(path_output, '{}_{}.pdf'.format(fname,i+1))  # 等价

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
                # print('生成文件:{}'.format(output_filename))


if __name__ == "__main__":
    # D:\Code\TimeVisual\ToolPy\pdf\社工档案袋1+2.pdf
    file_name = r"D:\Code\TimeVisual\ToolPy\pdf\社工档案袋1+2.pdf"
    file_path = r"D:\Code\TimeVisual\ToolPy\pdf"
    # pdf_split_1(file_name, file_path)
    pdf_split_2(file_name, file_path, 227, 530)
    # pdf_split_3(file_name, file_path, 9, 10)
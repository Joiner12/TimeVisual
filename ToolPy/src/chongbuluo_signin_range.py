#-*- coding:utf-8 -*-
"""
    1.使用request获取签到信息
    2.签到排名查看
    3.技术方案
        3.1 re
        3.2 beautifulsoap
        3.3 selenium:速度慢
        3.4 framedata合并
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from rich.progress import track


class cbl_range():
    response_page = str()
    web_cookies = dict()
    web_header = dict()
    web_proxy = dict()
    data_info = dict()

    def __init__(self) -> None:
        baseurl = r'https://www.chongbuluo.com/plugin.php?id=wq_sign&mod=info&ac=totaldays&page='
        # cookies
        cookies_str = "D43n_4dbf_smile=5D1; D43n_4dbf_ulastactivity=da6dNGsbzjCIivkEK1tbXYeHB7PREvv+Or+Yu0BZp2xH6NdObRFj; D43n_4dbf_lastcheckfeed=7184|1616374864; 1aG4_2132_nofavfid=1; _ga=GA1.2.1600461298.1617679672; 1aG4_2132_home_readfeed=1641259717; 1aG4_2132_editormode_e=1; 1aG4_2132_sid=0; 1aG4_2132_forum_lastvisit=D_117_1645062679D_125_1645412061D_2_1645518153D_93_1645518346D_119_1645669103D_112_1646727617D_120_1646727644D_98_1646882741D_113_1647224361; 1aG4_2132_saltkey=NYCfmldq; 1aG4_2132_lastvisit=1647389909; 1aG4_2132_auth=1477+ZcT2jEAIEnoT4wZL5EmmiVy3axRPXAaaVKIFc6jgWZGCzBOuJpguI6RD/e9nPeOZ1QyzhyIDCnDSe1PQNhK; 1aG4_2132_lastcheckfeed=7184|1647414724; 1aG4_2132_visitedfid=120D122D126D128D112D44D93D2D119D114; _gid=GA1.2.2134643030.1647507317; acw_tc=707c9fc716475640880652210e5007fc6038d8790aa680249ed658751a9a49; 1aG4_2132_ulastactivity=1647564088|0; 1aG4_2132_lastact=1647564303	plugin.php	"
        for line in cookies_str.split(';'):
            key, value = line.split('=', 1)
            self.web_cookies[key] = value
        # header
        self.web_header = {
            'Origin':
            'https://www.chongbuluo.com',
            'Referer':
            'https://at.alicdn.com/t/font_2463666_zj1hqsdx9w.css',
            'sec-ch-ua-platform':
            "Windows",
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
        }
        self.web_proxy = {
            'http_proxy': 'http://127.0.0.1:7890',
            'https_proxy': 'http://127.0.0.1:7890'
        }
        # find all page
        final_out = pd.DataFrame()
        for page_num in track(range(1, 600), 'Scraping'):
            cur_page_url = baseurl + str(page_num)

            # print(self._parsepage(url=cur_page_url))
            piece_fd = self._parsepage(url=cur_page_url)
            if page_num == 1:
                final_out = pd.DataFrame(columns=self.data_info['col'])
            # time.sleep(0.5)
            # print(time.ctime(), 'page:%.0f' % (page_num))
            print(piece_fd)
            final_out = final_out.append(piece_fd)
        final_out.to_csv('outlist.csv', encoding='gb18030')

    def _parsepage(
            self,
            url=r'https://www.chongbuluo.com/plugin.php?id=wq_sign&mod=info&ac=totaldays&page=1',
            *argv,
            **kwargv):

        html = requests.get(url,
                            cookies=self.web_cookies,
                            headers=self.web_header)
        if not html.status_code == 200:
            print("error")
            return
        soup = BeautifulSoup(html.text, 'lxml')
        return [
            self._parse_html_table(table) for table in soup.find_all('table')
        ]

    def _parse_html_table(self, table):
        n_columns = 0
        n_rows = 0
        column_names = []

        # Find number of rows and columns
        # we also find the column titles if we can
        for row in table.find_all('tr'):
            # Determine the number of rows in the table
            td_tags = row.find_all('td')
            if len(td_tags) > 0:
                n_rows += 1
                if n_columns == 0:
                    # Set the number of columns for our table
                    n_columns = len(td_tags)

            # Handle column names if we find them
            th_tags = row.find_all('th')
            if len(th_tags) > 0 and len(column_names) == 0:
                for th in th_tags:
                    column_names.append(th.get_text())

        # Safeguard on Column Titles
        if len(column_names) > 0 and len(column_names) != n_columns:
            raise Exception("Column titles do not match the number of columns")

        columns = column_names if len(column_names) > 0 else range(
            0, n_columns)
        self.data_info['col'] = columns
        df = pd.DataFrame(columns=columns, index=range(0, n_rows - 1))
        row_marker = 0
        for row in table.find_all('tr'):
            column_marker = 0
            columns = row.find_all('td')
            for column in columns:
                df.iat[row_marker, column_marker] = column.get_text()
                column_marker += 1
            if len(columns) > 0:
                row_marker += 1
            if row_marker > 6:
                break
        # Convert to float if possible
        for col in df:
            try:
                df[col] = df[col].astype(float)
            except ValueError:
                pass

        return df


if __name__ == "__main__":
    cbl = cbl_range()

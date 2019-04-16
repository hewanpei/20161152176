import re
from string import punctuation

text = open('������.txt')
text_list = text.readlines()
# ɾ����㼰�������÷���
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
text_plain = re.sub(r'[{}]'.format(punctuation), '', ''.join(text_list))
# ��дת��ΪСд��������ȷͳ�Ƶ�����
one_word_list = [word.lower() for word in text_plain.split()]
print(one_word_list)


def run_query(wanted):
    word_total = 0
    # ͳ�Ƴ��ֵ��ܸ���
    for each in one_word_list:
        if each == wanted:
            word_total += 1

    print('"{}" occurs {} times'.format(wanted, word_total))

    line_number = 0
    for line in text_list:
        line_plain = re.sub(r'[{}]'.format(punctuation), '', line)
        word_list = [word.lower() for word in line_plain.split()]
        # �����û�ϰ�ߵ�һ�д�"1"��ʼ
        line_number += 1
        # ÿ�еĵ����б�
        if wanted in word_list:
            # ���±�"0"��ʾ��һ�У�����Ҫ��ȥ1
            print('\tline {}: {}'.format(line_number, text_list[line_number - 1]), end='')


if __name__ == '__main__':
    while True:
        sought = input('Input a word you want to search: ')
        if sought == 'q':
            break

        run_query(sought)

import os

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if 'name, volumes' in line:
                continue
            name, volumes = line.strip().split(',')
            novel.append([name, volumes])
    return novels


def user_input(novels):
    while True:
        name = input('請輸入小說書名： ')
        if name == 'q':
            break
        volumes = input('請輸入該系列小說集數： ')
        novels.append([name, volumes])
    print(novels)
    return novels


def print_novels(novels):
    for novel in novels:
        print(novel[0], '系列共有', novel[1], '本書')


def write_file(filename, novels):
    with open(filename, 'w', encoding='utf-8')as f:
        f.write('novel,series\n')
        for novel in novels:
            f.write(novel[0] + ',' + novel[1] + '\n')


def main():
    filename = 'novels.csv'
    if os.path.isfile(filename):
        print('We got the file!!!')
    else:
        print('Sorry...File cannot be found.')

    novels = []
    novels = user_input(novels)
    print_novels(novels)
    write_file('novels.csv', novels)


if __name__ == '__main__':
    main()
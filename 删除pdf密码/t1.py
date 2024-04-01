# python实现pdf文档的解密
from PyPDF2 import PdfReader #pdf的读取方法
from PyPDF2 import PdfWriter #pdf的写入方法
from Crypto.Cipher import AES #高加密的方法，要引入不然会报错

def get_reader(filename, password): #读取pdf的方法（自定义函数）
    try:
        old_file = open(filename, 'rb')
        print('解密开始...')
    except Exception as err:
        return print('文件打开失败！' + str(err))

    #如果是python2将PdfReader改为PdfFileReader
    pdf_reader = PdfReader(old_file, strict=False) #读取pdf文件

    # 如果是python2将is_encrypted改为isEncrypted
    if pdf_reader.is_encrypted: #解密操作（以下操作是自适应，不会展示在终端中）
        if password is None:
            return print('文件被加密，需要密码！--{}'.format(filename))
        else:
            if pdf_reader.decrypt(password) != 1:
                return print('密码不正确！--{}'.format(filename))
    elif old_file in locals():
        old_file.close() #如果pdf文件已经在本地了就关闭
    return pdf_reader #返回读出pdf的值

    
def deception_pdf(filename, password, decrypted_filename=None): #生成新pdf的方法（自定义函数）
    print('正在生成解密...')
    pdf_reader = get_reader(filename, password) #得到传入的文件名，和密码（如果密码没有可以不填）
    if pdf_reader is None:
        return print("无内容读取")

    # 如果是python2将is_encrypted改为isEncrypted
    elif not pdf_reader.is_encrypted:
        return print('文件没有被加密，无需操作')

    # 如果是python2将PdfWriter改为PdfFileWriter
    pdf_writer = PdfWriter() #写pdf（记录pdf内容）

    #如果是python2将append_pages_from_reader改为appendPagesFromReader
    pdf_writer.append_pages_from_reader(pdf_reader)

    if decrypted_filename is None: #创建解密后的pdf文件和展示文件的路径
        decrypted_filename = "".join(filename.split('.')[:-1]) + '_' + '已解密' + '.pdf'
        print("解密文件已生成:{}".format(decrypted_filename))
    # 写入新文件
    pdf_writer.write(open(decrypted_filename, 'wb'))

if __name__ == '__main__':
    # 逗号前面的为需要解密的pdf文件路径，后面的''里面为密码，如果不知道就用不填
    deception_pdf("G:\\python学习专用\\2024\\删除pdf密码\\顶管施工中土体性状及环境效应分析_魏纲.pdf", '')

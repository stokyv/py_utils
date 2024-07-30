from bs4 import BeautifulSoup

html_string = '''<option value="">- Chọn -</option>
<option value="031">Huyện Bắc Mê</option>
<option value="034">Huyện Bắc Quang</option>
<option value="032">Huyện Hoàng Su Phì</option>
<option value="027">Huyện Mèo Vạc</option>
<option value="029">Huyện Quản Bạ</option>
<option value="035">Huyện Quang Bình</option>
<option value="030">Huyện Vị Xuyên</option>
<option value="033">Huyện Xín Mần</option>
<option value="028">Huyện Yên Minh</option>
<option value="026">Huyện Đồng Văn</option>
<option value="024">Thành phố Hà Giang</option>
'''
#view district in provice
 #https://guland.vn/get-sub-location?id=75&is_bds=1 #xem quận huyện trong Đồng Nai

#view ward in a district
#https://guland.vn/get-sub-location?id=739&type=district #xem xã trong huyện Cẩm Mỹ

soup = BeautifulSoup(html_string, 'html.parser')

# Find all option tags
options = soup.find_all('option')

# Extract value and text for each option
for option in options:
    value = option.get('value')
    text = option.text
    print(f"Value: {value}, Text: {text}")



#Tạo csv với columns sau: id, type, name
# type = ['province', 'district', 'ward']
# '031', 'province', "TPHCM"
# '242421', 'ward', 'xã dieg fedf'
#sort by id
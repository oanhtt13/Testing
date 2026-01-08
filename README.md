# TÀI LIỆU HLD

# MỤC LỤC
# [I. Giới thiệu](#i-giới-thiệu)
## [1.1.Mục đích chung](#11-mục-đích-chung)
## [1.2. Phạm vi](#12-phạm-vi)
## [1.3. Định nghĩa và từ viết tắt](#13-định-nghĩa-và-từ-viết-tắt)
## [1.4. Các yêu cầu chính](#14-các-yêu-cầu-chính)

# [II. Tổng quan hệ thống và các thành phần chính](#ii-tổng-quan-hệ-thống-và-các-thành-phần-chính)
## [2.1. Mô tả](#21-mô-tả)
## [2.2. Giới thiệu phần cứng](#22-giới-thiệu-phần-cứng)
## [2.3. Sơ đồ kiến trúc](#23-sơ-đồ-kiến-trúc)

# [III. Thu thập và xử lý dữ liệu](#iii-thu-thập-và-xử-lý-dữ-liệu)
## [3.1. Thu thập dữ liệu](#31-thu-thập-dữ-liệu)
## [3.2 Lọc dữ liệu ảnh](#32-lọc-dữ-liệu-ảnh)
## [3.3. Gán nhãn dữ liệu](#33-gán-nhãn-dữ-liệu)

# [IV.Huấn luyện model AI](#iv-huấn-luyện-model-ai)
## [4.1. Chia dữ liệu](#41--chia-dữ-liệu)
## [4.2. Data testing](#42-data-testing)

# [V. Convert Model](#v-convert-model-ai)

# [VI. Inference App](#vi-inference-avi)
## [6.1. Mô tả](#61-mô-tả)
## [6.2. Hướng dẫn sử dụng ứng dụng](#62-hướng-dẫn-sử-dụng-ứng-dụng)

# [VII. Công nghệ và nền tảng](#vii-công-nghệ-và-nền-tảng)

# [VIII. Giao diện bên ngoài](#viii-giao-diện-bên-ngoài)

# [IX. Cấu hình](#ix-cấu-hình)

# [X. ErrorXhandling](#x-error-handling)

# [XI. Các khía cạnh phi chức năng](#xi-các-khía-cạnh-phi-chức-năng)

# [XII. Phụ lục](#xii-phụ-lục)

## I. GIỚI THIỆU

### 1.1. Mục đích chung

Dự án giúp phát hiện xe đang di chuyển tại vỉa hè hay lòng đường bằng cách tích hợp AI với phần cứng khách hàng cũng cấp.
Phần cứng khách hàng bao gồm:
1. Mạch phần cứng Rockchip RK1808 EVB V10 Board
2. Module Camera.

Dự án hiện tại có 2 ứng dụng cần phát triển:
+ Collect data software: ứng dụng hỗ trợ thu thập dữ liệu, chụp ảnh, lưu vào bộ nhớ.
+ Main software: ứng dụng phát hiện xe đạp đang di chuyển tại vỉa hè hay làn đường.

### 1.2. Phạm vi

#### Thu thập dữ liệu
- Địa điểm: Nhật Bản - khách hàng đã cung cấp các vị trí cụ thể để thu thập dữ liệu.

![Maps](img/maps.jpg)

- Số lượng ảnh cần thu thập: target: 10000 raw images.
- Số lượng ảnh sử dụng: 4500 images.
- Các kịch bản thu thập dữ liệu: [Scenario](https://docs.google.com/spreadsheets/d/1dLg0KzIUWV-L5fPBXcsZgAe5XzseXncuVe0B2Jg_9lE/edit?gid=0#gid=0).

#### Huấn luyện mô hình AI:

- Sử dụng model AI cho semantic segmentation: DDRNet23-Slim

#### Triển khai ứng dụng

Để triển khai ứng dụng được trên thiết bị phần cứng khách hàng cung cấp:

- Convert model sang định dạng RKNN.

### 1.3 Định nghĩa và từ viết tắt

|Word| Explain |Meaning|
|---|---|---|
|Device| Device| Thiết bị phần cứng khách hàng cung cấp|
|EMA| Exponential Moving Average| Thuật toán hỗ trợ làm mịn|
|PC|Pesonal Computer| Máy tính cá nhân|
|Console|Console| Giao diện dòng lệnh: <br> Window: **Power Sheel** <br> Ubuntu/MacOS: **Terminal**|

### 1.4. Các yêu cầu chính
- Phân biệt được làn đường và vỉa hè.
- Cần đưa ra được vị trí tương đối của xe đạp khi xe đang tham gia giao thông (đang đi trên vỉa hè hay lòng đường).
- Cần lưu ảnh sau khi xC lý để có thể thực hiện đánh giá model.
- Tốc độ xử lý: tối thiểu 2fps.

## II. TỔNG QUAN HỆ THỐNG VÀ CÁC THÀNH PHẦN CHÍNH

### 2.1. Mô tả

Hệ thống được chia thành 3 giai đoạn chính: Thu thập dữ liệu, Mô hình AI và Phát triển ứng dụng.

Hệ thống gồm 2 phần:
+ Device: Mạch phần cứng + Camera.
+ PC: cho phép kết nối với thiết bị qua ADB Interface, sau đó có thể truy cập, điều khiển, trích xuất thông tin từ thiết bị.

### 2.2 Giới thiệu phần cứng

#### 2.2.1 Thông số thiết bị phần cứng

* Thiết bị: Rockchip RK1808 EVB V10 Board
* Bộ xử lý: Rockchip RK1808 NPU, performance: 3 TOPS (Trillions of Operations Per Second)
* Hỗ trợ: INT8, INT16, FP16 quantization
* RAM: 2 GB
* Bộ nhớ:
    * Root filesystem: 2.6 GB (1.3 GB còn trống)
    * User data: 4.0 GB (1.7 GB còn trống)
* Hệ điều hành: OS Linux Embedded

#### 2.2.2 Cầu trúc folder

```
/userdata/
├── models/
│   └── ddrnet_rk1808.rknn          (File model AI - KHÔNG XÓA)
│
├── captures/                        (Thư mục gốc chứa tất cả dữ liệu)
│   ├── captures1/                   (Phiên làm việc 1)
│   │   ├── raw/                     (Ảnh gốc từ camera)
│   │   ├── segmented/               (Ảnh phân đoạn màu)
│   │   ├── overlay/                 (Ảnh kết hợp raw and segment)
│   │   └── position.log             (Log vị trí)
│   │
│   └── captures2/                   (Phiên làm việc 2)
│       └── ...
│
└── service/
    ├── config.json                  (File cấu hình - QUAN TRỌNG)
    ├── service.py                   (Code chương trình)
    └── model.py                     (Chương trình load model)
```

### 2.3. Sơ đồ kiến trúc

![Architecture](<img/Slice 9.png>)

#### 2.3.1 Luồng tương tác giữa thiết bị và PC

![Architecture](img/system_architecture.jpg)

## III. THU THẬP VÀ XỬ LÝ DỮ LIỆU

### 3.1 Thu thập dữ liệu

Ứng dụng thu thập dữ liệu (Collect Data Software) bằng cách chụp ảnh tự động liên tục từ camera với chu kỳ 5 giây và lưu trữ với tên file theo thời gian thực.

#### 3.1.1. Các chức năng chính
- Chụp ảnh tự động theo chu kỳ.
- Lưu ảnh và đặt tên theo thời gian thực (timestamp).
- Kiểm tra dung lượng ổ đĩa trước khi chụp.
- Tự động dừng khi dung lượng đĩa thấp hơn ngưỡng cho phép.

#### 3.1.2. Quy trình vận hành

Thiết bị RK1808 được cấu hình để chạy script chụp ảnh tự động ngay khi được cấp nguồn. Script sẽ khởi động và hoạt động độc lập mà không cần can thiệp thủ công. Quy trình vận hành ứng dụng như sau: 

1. Khởi động tự động:
Thiết bị tự động chạy ứng dụng khi kết nối dây nguồn.
2. Cấu hình:
Sử dụng ADB Interface để kết nối với máy tính cá nhân.
3. Triển khai script:
Đẩy chương trình và cấu hình lên thiết bị thông qua ADB
4. Giám sát: 
Kiểm tra log và tình trạng hoạt động qua kết nối ADB

#### 3.1.3. Sơ đồ khối ứng dụng

![Tool Flow](img/tool_flow.jpg)

#### 3.1.4. Thư viện cần thiết trên device

| Component | Technology |
|-----------|-----------|
| Programming Language | Python 3.x |
| Computer Vision Library | OpenCV (cv2) |
| Operating System | Linux-based (userdata path) |
| Camera Interface | Video4Linux (V4L) |

#### 3.1.5. Hướng dẫn chuẩn bị cài đặt ứng dụng

**Cài đặt trên Windows OS**

*Sử dụng Android SDK Platform-Tools*

1. Download SDK Platform-Tools:

    * Truy cập: [Platform Tool](https://developer.android.com/tools/releases/platform-tools)
    * Tải file ứng dụng dành cho Window OS.
    * Thêm vào PATH:

        Nhấn ``Win + X``

        Chọn ``System``

        Chọn ``Advanced system settings``

        Click ``Environment Variables``

        Trong ``System variables``, tìm và chọn ``Path`` -> Click ``Edit``
        
        Click ``New`` và thêm ``C:\platform-tools``

        Click ``OK``.

    * Kiểm tra cài đặt

        Nhấn nút ``Windown``

        Gõ tìm kiếm ứng phụ **Power Shell**

        Nhấn ``Enter``

        Chạy lệnh tại của sổ ứng dụng:

        ```
        adb version
        ```

        Thông tin ứng dụng hiển thị lên màn hình thông báo ứng dụng đã được cài đặt thành công

**Cài đặt trên Linux (Ubuntu/Debian)**

1. Cập nhật package list

    ``` bash
    sudo apt update
    ```

2. Cài đặt abd
    
    ```bash
    sudo apt install adb -y
    ```

3. Kiểm tra phiên bản

    ```
    adb version
    ```

#### 3.1.6. Cài đặt ứng dụng cho thiết bị

**1. Download chương trình về PC**

Download source code tại: [Collect data application](https://git.hblab.vn/rnd/pro-1769-bike-camera-segmentation.git)

**2. Giải nén source code**

Sử dụng công cụ có sẵn trên PC để giải nén file vừa tải về.

**3. Kết nối thiết bị với PC**

* Thực hiện cắm nguồn, kết nối thiết bị vào máy tính cá nhân qua cổng USB.
* Mở **Terminal** hoặc **Power Shell** trên PC.
* Kiểm tra kết nối giữa thiết bị và máy tính thông qua lệnh:

```
adb devices
```

* Trường hợp thiết bị chưa kết nối thành công:

![fail_connect_device](img/fail_connect_device.png)

**4. Cài đặt ứng dụng**

* Khi Terminal xuất hiện thiết bị, tiến hành chạy lệnh
```
adb push {path/to/service/code/file} userdata/
```

**Reboot thiết bị**

**Cách 1:** Rút nguồn thiết bị cắm lại

**Cách 2:** Chạy lệnh sau tại **Console:**
```
adb shell reboot
```

**Đảm bảo thiết bị đã chạy**
Check ``log file`` theo hướng dẫn:

Chạy lệnh tại **Console** trên PC:

```
adb pull userdata/app_log.txt {path/to/save (optional)}
```
App chạy thành công:

![log_file]()

**5. Get images from device to PC**

Sau khi thu thập dữ liệu có thể tiến hành lấy ảnh từ thiết bị về PC để xử lý theo hướng dẫn sau:

**Bước 1:** Kết nối thiết bị với máy tính cá nhân tương tự với hướng dẫn tại [Kết nối thiết bị với PC](#316-cài-đặt-ứng-dụng-cho-thiết-bị)

**Bước 2:** Thực hiện lệnh sau để download ảnh về PC:
```
adb pull userdata/captures {path/to/save (optional)}
```
*Note*:

``adb pull``: download file/folder từ device về PC
``adb push``: upload file/folder từ PC sang device

**6. Xóa ảnh**

**Bước 1:** Kết nối thiết bị với máy tính cá nhân tương tự với hướng dẫn tại [Kết nối thiết bị với PC](#316-cài-đặt-ứng-dụng-cho-thiết-bị)

**Bước 2:** Thực hiện lệnh sau để xóa folder chứa ảnh:

```
adb shell "rm -r userdata/captures"
```

### 3.2 Lọc dữ liệu ảnh

Việc lọc dữ liệu ảnh trước khi gãn nhãn giúp loại bỏ ảnh nhiễu, ảnh kém chất lượng và dữ liệu trùng lặp. Từ đó đảm bảo nhãn chính xác, tiết kiệm thời gian và chi phí. Bên cạnh đó, dữ liệu sạch sẽ tạo ra mô hình AI có độ chính xác cao hơn và khả năng tổng quát hóa tốt khi sử dụng thực tế.

Các phương pháp lọc dữ liệu:

* Loại bỏ ảnh trùng lặp
* Loại bỏ ảnh chất lượng thấp
* Loại bỏ dữ liệu ngoại lai

### 3.3 Gán nhãn dữ liệu
Sau khi đã lọc dữ liệu, tiến hành gán nhãn dữ liệu.
Target: 4500 images.

Sử dụng công cụ hỗ trợ annotation có sẵn trên thị trường.

#### 3.3.1 Hướng dẫn annotation

Với bài toàn hiện tại, có 3 label sẽ được tiến hành khoanh vùng:

1. Road
2. Side walk
3. Other

#### 3.3.2 Rule label

##### 3.3.2.1 Annotation for segment AI Model

**Road:**

1. Lòng đường là khu vực các xe (bao gồm xe đạp, ô tô, xe máy, ...) di chuyển chung.
2. Khu vực bên phải lan can.

**Side Walk:**

1. Khu vực dành cho người đi bộ, phần nằm dọc hai bên đường, cao hơn đường chính.
2. Phần đường vỉa hè nhưng xe đạp vẫn có thể đi lên vẫn nhận diện là vỉa hè.
3. Vỉa hè thường nằm bên trái của lan can.

**Other:**

1. Khu vực còn lại sau khi nhận diện *Road* và *Sidewalk*.

**Example:**

*Note:*
* Pink: Side walk
* Grey: Road
* Black: Other

![sample_1](img/sample_1.png)

![sample_2](img/sample_2.png)

![sample_3](img/sample_3.png)

##### 3.3.2.1 Annotation for bike's location

Dựa theo dữ liệu của việc thu thập data, tiến hành sử dụng tool label ảnh thu thập:

**Example:**

![location_1](img/sample_location_1.png)

![location_2](img/sample_location_2.png)

## IV. HUẤN LUYỆN MODEL AI

### 4.1  Chia dữ liệu

Dữ liệu ảnh được chia thành 2 phần:

* Dataset for training.
* Dataset for testing.

#### 4.1.1 Data training

Dữ liệu ảnh được sử dụng để huấn luyện mô hình:
- Số lượng: 6700 ảnh
- Bao gồm: 3800 ảnh từ dữ liệu đã thu thập (cần phải annotate) và 2900 ảnh từ dữ liệu public (không cần phải annotate).

#### 4.1.2 Data testing

Dữ liệu ảnh được sử dụng để kiểm thử chia thành 2 loại:
- Dữ liệu cho kiểm thử segment AI model.
- Dữ liệu cho kiểm thử phần xác định vị trí xe đạp.

**Dữ liệu cho kiểm thử model**

Dữ liệu cho phần kiểm thử tiếp tục được phân chia theo từng kịch bản khác nhau. Số lượng ảnh trên từng kịch bản tham khảo [tại đây](https://docs.google.com/spreadsheets/d/1dLg0KzIUWV-L5fPBXcsZgAe5XzseXncuVe0B2Jg_9lE/edit?gid=0#gid=0).

**Dữ liệu cho kiểm thử phần xác định vị trí xe đạp**

- Số lượng: 600 ảnh.

## V. Convert model AI

Để sử dụng được thiết bị trên thiết bị phần cứng, model cần phải được convert như sau:

![Convert mode](<img/Convert model.png>)

## VI. INFERENCE APP

### 6.1 Mô tả

Ứng dụng có các tính năng chính sau:
* Lấy dữ liệu ảnh từ camera
* Xử lý qua model AI
* Phát hiện vị trí xe đạp, lưu lại dữ liệu

**Luồng hoạt động ứng dụng**

![Inference Appp](<img/inference app.png>)

#### 6.1.1 Lấy dữ liệu ảnh từ Camera

* Đọc file config
* Chụp ảnh bằng camera
* Xử lý ảnh theo cài đặt trong file config (resize)
* Lưu ảnh theo thông tin trong file config

#### 6.1.2 Model AI

Ảnh sau khi qua post-processing sẽ được đưa vào model AI giúp xác định vị trí road và sidewalk.

Kết quả: Từng pixel ảnh được đánh dấu label ``road``, ``side``, ``other``.

#### 6.1.3 Phát hiện vị trí xe đạp và lưu dữ liệu

##### 6.1.3.1 Xác định vị trí xe đạp

Sau khi phát hiện được vị trí của road và sidewalk, chúng tôi sử dụng phương pháp heuristic-only để xác định vị trí của xe đạp.

![alt text](img/post-processing.png)

**Xác định vị trí xe**

Luồng xử lý:

* Cắt một vùng ảnh chứa nhiều thông tin cần thiết.
* Tính số lượng pixel được gán nhãn ``road`` và ``side walk``.
* Tính toán công thức: $$ ratio = {road\over road+sidewalk}$$

* Quyết định:

Set `threshold = 0.6`

$ratio \ge threshold$ : xe di chuyển trên đường

$ratio < thresold$: xe di chuyển trên vỉa hè

![alt text](img/location.png)

##### 6.1.3.2 Tăng độ chính xác khi di chuyển trên đường thật

Vì xe di chuyển trên đường, nên không thể tránh khỏi các trường hợp hình ảnh bị rung, lắc, mờ, nhiễu, hoặc lệch vị trí camera tạm thời dẫn đến AI đánh giá sai một vài khung hình. Để tăng độ chính xác cho việc phát hiện vị trí xe đạp, chúng tôi đề xuất quy trình xử lý như sau:

**Phương pháp làm mịn EMA**

Phương pháp giúp điều chỉnh lại ratio của từng khung hình dựa trên các khung hình trước đó.

Luồng xử lý:

* Bắt đầu từ frame thứ 5
* Tiền hành tính toán lại ``ratio`` mỗi frame theo công thức:
$$ r_i = 0.2(r_i + r_{i-1}+ r_{i-2}+r_{i-3}+r_{i-4})$$
* Gán giá trị ``ratio`` mới vào ảnh

![alt text](img/EMA.png)

**Phương pháp Deboucing**

Phương pháp giúp gán lại nhãn cho khung hình dựa trên dữ liệu ảnh trước đó.
Xử lý sau khi lấy dữ liệu từ EMA.

Luồng xử lý:

* Bắt đầu từ frame thứ 4
* Đánh giá label vị trí:

Nếu $(r_{i-1}) \& (r_{i-2}) \& (r_{i-3}) \ge threshold$: location ``road``

Nếu $(r_{i-1}) \& (r_{i-2}) \& (r_{i-3})< threshold$: location ``sidewalk``

Nếu $(r_{i-1}) || (r_{i-2}) || (r_{i-3})< threshold$: location sẽ dựa rên ratio

![alt text](img/Deboucing.png)

##### 6.1.3.3 Lưu dữ liệu vào bộ nhớ

Sau khi hoàn tất xử lý, ứng dụng tiến hành lưu thông tin vào bộ nhớ. Thông tin lưu trữ bao gồm:
* Ảnh raw
* Ảnh sau khi segemnt
* Ảnh ghép chung giữa ảnh raw và ảnh segement: giúp hỗ trợ cho phần đánh giá kết quả
* Position log: vị trí xe đạp theo fomat: ``image_name + lable``
* App log: log hoạt động của thiết bị.

Các thông tin sẽ được lưu lại vào folder tương ứng: [Cấu trúc folder](#222-cầu-trúc-folder)

### 6.2 Hướng dẫn sử dụng ứng dụng

**Bước 1:** Cài đặt ứng dụng

Cài đặt ứng dụng theo hướng dẫn: [Hướng dẫn cài đặt](#316-cài-đặt-ứng-dụng-cho-thiết-bị)

**Bước 2:** Update file config

File `config` cần được tạo trên PC với fomat sau:

Định dạng file `.json`
```json
 {
  "mode": "running",
  "processing_mode": "capture-segment",
  "model_path": "/userdata/models/ddrnet_rk1808.rknn",
  "base_dir": "/userdata/captures",
  "interval": 0.5
}
```

|Key|Value|
|---|---|
|mode| Chế độ hoạt động: <br> `running`: Chạy chương trình <br> `paused`: Tạm dừng chương trình <br> `stopped`: Thoát chương trình|
|processing_mode| Chế độ xử lý: <br> `capture-only`: Thu thập dữ liệu ảnh <br> `capture-segment`: Ứng dụng suy luận|
|model_path| Đường dẫn đến thư mục lưu trữ model|
|base_dir| Đường dẫn đến thư mục chứa ảnh sau xử lý|
|interval| Thời gian giữa hai lần chụp ảnh gần nhất. Đơn vị: `giây`|

**Bước 3:** Đẩy file config vào device

Tại folder chứa file config trên PC, mở **Console**

Run:

```
adb push path/to/config/file userdata/service/config.json
```
Ứng dụng sẽ hoạt động theo cài đặt trong file config

## VII. CÔNG NGHỆ VÀ NỀN TẢNG

### 1. Thiết bị phần cứng

- Cục cấp nguồn
- Thiết bị RK1808 (Rockchip AI Processing Unit)
- Camera Module (Camera ID: 6)
- Bộ nhớ lưu trữ: /userdata

### 2. Máy tính cá nhân

- Hệ điều hành: Linux/Windows/MacOS
- Công cụ: ADB (Android Debug Bridge)

### 3. Công nghệ sử dụng trên device

- Ngôn ngữ lập trình: Python 3.x
- Thư viện xử lý ảnh: OpenCV (cv2)
- Logging: Python logging module
- Hệ điều hành thiết bị: Linux-based
- Interface kết nối: ADB (Android Debug Bridge)

## VIII. GIAO DIỆN BÊN NGOÀI

- Không có giao diện đồ họa
- Tương tác qua log file và Console

## IX. CẤU HÌNH

| Tham số | Giá trị | Mô tả |
|---------|---------|-------|
| CAMERA_ID | 6 | ID của camera trên thiết bị |
| SAVE_PATH | ```/userdata/captures/``` | Đường dẫn lưu ảnh |
| LOG_FILE | ```/userdata/app_log.txt``` | Đường dẫn file log |
| CAPTURE_INTERVAL | 5 giây | Chu kỳ chụp ảnh |
| MIN_FREE_SPACE_MB | 1000 MB | Ngưỡng dung lượng tối thiểu |
| APPROX_IMAGE_SIZE_KB | 100 KB | Kích thước ước tính mỗi ảnh |
| Định dạng file | ```capture_YYYYMMDD_HHMMSS.jpg``` | Format tên file ảnh |

## X. ERROR HANDLING

| Loại Lỗi | Phát Hiện | Xử Lý |
|-----------|-----------|--------|
| Camera không khả dụng | ``` cap.isOpened() == False``` | Ghi log lỗi và thoát chương trình |
| Chụp frame thất bại | ```ret == False``` | Ghi log lỗi và tiếp tục vòng lặp |
| Dung lượng đĩa thấp | ```free_space < MIN_FREE_SPACE_MB``` | Ghi log cảnh báo và dừng chụp |
| Lỗi không xác định | ```Exception``` | Ghi log lỗi, đóng camera và thoát |

## XI. CÁC KHÍA CẠNH PHI CHỨC NĂNG

### 1. Hiệu suất
- Thời gian chụp mỗi ảnh: < 1 giây
- Chu kỳ chụp: 5 giây/ảnh
- Kích thước ảnh: ~100 KB/ảnh
- Dung lượng lưu trữ ước tính: ~10 MB cho 100 ảnh

### 2. Độ tin cậy
- Tự động kiểm tra dung lượng đĩa trước mỗi lần chụp
- Logging đầy đủ để theo dõi và debug
- Xử lý exception để tránh crash

### 3. Khả năng bảo trì
- Code có cấu trúc rõ ràng, dễ đọc
- Các tham số cấu hình tập trung ở đầu file
- Logging chi tiết giúp troubleshooting

### 4. Mục tiêu dự án (Main Software - AI Model)
- Độ chính xác: mIoU >= 70% trên tập dữ liệu kiểm thử độc lập
- Thời gian xử lý: Real-time inference trên RK1808
- Model format: ONNX

## XII. PHỤ LỤC

### 1. Ví dụ Log Output

```
2025-10-17 09:00:00 - INFO - Vision app started...
2025-10-17 09:00:00 - INFO - Camera ID: 6
2025-10-17 09:00:00 - INFO - Save path: /userdata/captures/
2025-10-17 09:00:00 - INFO - Capture interval: 5 seconds
2025-10-17 09:00:00 - INFO - Minimum free space threshold: 1000 MB
2025-10-17 09:00:00 - INFO - Initial free disk space: 5234.56 MB
2025-10-17 09:00:00 - INFO - Estimated max images before threshold: ~43345
2025-10-17 09:00:01 - INFO - Camera opened successfully
2025-10-17 09:00:01 - INFO - Captured #1: /userdata/captures/capture_20251017_090001.jpg
2025-10-17 09:00:06 - INFO - Captured #2: /userdata/captures/capture_20251017_090006.jpg
...
2025-10-17 09:00:51 - INFO - Captured #10: /userdata/captures/capture_20251017_090051.jpg (Free: 5233.56 MB)
```

### 2. Lệnh ADB hữu ích

```bash
# Kiểm tra kết nối thiết bị
adb devices

# Kiểm tra dung lượng trống
adb shell df -h /userdata

# Xem log real-time
adb shell tail -f /userdata/app_log.txt

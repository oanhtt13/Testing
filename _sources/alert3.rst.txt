.. role:: red

Alert 3
============

Overview
--------------

Cho phép xác định bệnh nhân thuộc Alert 3 dựa trên các điều kiện khách hàng cung cấp. Đây là luồng đã có, cần update lại danh sách các điều kiện.

.. list-table:: **FR-Alert_3-1: Alert 3 Feature**
   :header-rows: 1
   :widths: 30 80 

   * - Content
     - Detail
   * - Description
     - Cho phép xác định bệnh nhân thuộc Alert 3 dựa trên các điều kiện khách hàng cung cấp. Đây là luồng đã có, cần update lại danh sách các điều kiện (Được chú thích tại bảng dưới)
   * - Input
     - Danh sách bệnh nhân cần được phân loại

       Danh sách các bệnh của bệnh nhân được lấy từ database ``mst_diseases``

       Danh sách các loại thuốc đặc biệt lấy từ database ``mst_special_medicines``

       Danh sách các keyword được lấy từ database ``mst_keyword``
   * - Output
     - Danh sách bệnh nhân sau khi đã được loại bỏ bệnh nhân có Alert 3.
   * - Trigger
     - Sau khi lấy được danh sách bệnh nhân

       Trước khi chạy model (do các bệnh nhân có alert 3 sẽ không được tính phí)
   * - Preconditions
     - Các bảng trong database được update đầu đủ:

       ``patient_list``

       ``patient_disease``

       ``mst_keyword``

       ``mst_special_medicines``

       ``doctor_comment``
   * - Postconditions
     - Update thông tin vào bảng ``tbl_record`` các cột sau:

       ``severse_status``

       ``nursing_flag``

       ``severe_type_1``

       ``severe_type_2``

       ``severe_type_3``

       ``cancer_test_flag``

       ``special_medical_flag``

       ``alert_keyword_flag``

       ``alert_type_3``

       ``alert_type_3_evidence``

.. list-table:: **Business Logic**
   :header-rows: 1
   :widths: 20 80 50

   * - Step
     - Business Logic
     - Business Logic Acceptance Criteria
   * - 1. Lấy danh sách bệnh nhân
     - Lấy danh sách bệnh nhân cần được phân loại
     - Với danh sách bệnh nhân trước model 1: lấy danh sách record đã crawl được của 1 clinic từ start_date đến end_date
       Với danh sách bệnh nhân trước model 2: Toàn bộ các bản record trong database.
   * - 2. Gán nhãn bệnh nhân có Alert3
     - :red:`severe_status`

       **Nếu**:

       Bệnh nhân có thông tin ``management_section`` là ``在重`` hoặc ``施重``

       **Thì**:

       Bệnh nhân được ghi nhận có thông tin ``severe_status`` (gán bằng 1)

       :red:`nursing_flag`

       **Nếu:**

       Bệnh nhân có thông tin ``record_label`` là ``訪問看護`` hoặc ``点滴``

       **Thì:**

       Bệnh nhân được gán cờ ``nursing_flag``

       :red:`severe_type_1`

       **Nếu:**

       Bất kì bệnh nào của bệnh nhân cũng thuộc trong danh sách các bệnh trong bảng ``mst_disease`` (bệnh khó chữa)

       **Thì:**

       Bệnh nhân được gán cờ ``severe_type_1``

       :red:`severe_type_2`

       **Nếu:**

       Bất kì bệnh nào của bệnh nhân thuộc trong danh sách các bệnh trong cột ``keywords`` có ``type``:``managerment_diseases``

       **Thì:**

       Bệnh nhân được gán cờ ``severe_type_2``

       :red:`severe_type_3`

       **Nếu:**

       Bệnh nhân có trường ``burden_rate`` chứa đoạn text ``難病``

       **Thì:**

       Bệnh nhân được gán cờ ``severe_type_3``

       :red:`cancer_test_kw`

       **Nếu:**

       Bất kì trong cột ``keyword`` có ``type``: ``cancer_test``

       **Thì:**

       Bệnh nhân được gán cờ ``cancer_test_flag``

       :red:`special_medical_flag`

       **Nếu:**

       sdgsdg

       **Thì:**

       sdgsdgsfg

       :red:`alert_keyword_flag`

       **Nếu:**

       fhdfhdf

       **Thì:**

       fgfgfg

     - Lưu thông tin vào database
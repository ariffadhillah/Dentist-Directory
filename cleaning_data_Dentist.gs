// function highlightDuplicates() {
//     var ss = SpreadsheetApp.getActiveSpreadsheet();
//     var sheets = ["ONCD"]; // Nama sheet
//     // var sheets = ["ONCD", "Annuaire Améli", "Invisalign", "Annuaire dentaire", "Doctolib"]; // Nama sheet

//     sheets.forEach(sheetName => {
//         var sheet = ss.getSheetByName(sheetName);
//         if (!sheet) return;

//         var range = sheet.getDataRange();
//         var values = range.getValues();
//         var nameCol = 1;  // Kolom Name (B)
//         // var specialiteCol = 2;  // Kolom Spécialité (C)
//         var addressCol = 3;  // Kolom Address (D)

//         var uniqueSet = new Set();
//         var duplicateRows = [];

//         for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
//             var key = values[i][nameCol] + values[i][addressCol];
//             if (uniqueSet.has(key)) {
//                 duplicateRows.push(i + 1); // Tambah 1 karena Google Sheets berbasis 1 (bukan 0)
//             } else {
//                 uniqueSet.add(key);
//             }
//         }

//         var rangeList = duplicateRows.map(row => sheet.getRange(row, 1, 1, sheet.getLastColumn()));
//         rangeList.forEach(range => range.setBackground("green").setFontColor("white"));
//     });
// }



// // function highlightDuplicates() {
// //     var ss = SpreadsheetApp.getActiveSpreadsheet();
// //     // var sheets = ["ONCD", "Annuaire Améli", "Invisalign", "Annuaire dentaire", "Doctolib"]; // Nama sheet
// //     var sheets = ["ONCD"]; // Nama sheet

// //     sheets.forEach(sheetName => {
// //         var sheet = ss.getSheetByName(sheetName);
// //         if (!sheet) return;

// //         var range = sheet.getDataRange();
// //         var values = range.getValues();
// //         var nameCol = 1;  // Kolom Name (B)

// //         var uniqueSet = new Set();
// //         var duplicateRows = [];

// //         for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
// //             var key = values[i][nameCol]; // Hanya gunakan "Name" sebagai kunci pencarian
// //             if (uniqueSet.has(key)) {
// //                 duplicateRows.push(i + 1); // Tambah 1 karena Google Sheets berbasis 1 (bukan 0)
// //             } else {
// //                 uniqueSet.add(key);
// //             }
// //         }

// //         var rangeList = duplicateRows.map(row => sheet.getRange(row, 1, 1, sheet.getLastColumn()));
// //         rangeList.forEach(range => range.setBackground("red").setFontColor("white"));
// //     });
// // }




// // untuk melihat jumlah duplicate
// function highlightDuplicates() {
//     var ss = SpreadsheetApp.getActiveSpreadsheet();
//     var sheets = ["ALL Dentist"]; // Nama sheet

//     sheets.forEach(sheetName => {
//         var sheet = ss.getSheetByName(sheetName);
//         if (!sheet) return;

//         var range = sheet.getDataRange();
//         var values = range.getValues();
//         var nameCol = 1;  // Kolom Name (B)
//         var addressCol = 3;  // Kolom Address (E)
//         var postal_code = 4;  // Kolom Postal code (F)
//         var city_ = 5;  // Kolom City (G)

//         var uniqueSet = new Set();
//         var duplicateRows = [];
//         var duplicateCount = 0;

//         for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
//             var key = values[i][nameCol] + values[i][postal_code] + values[i][city_]; // Gabungan Name + Address
//             if (uniqueSet.has(key)) {
//                 duplicateRows.push(i + 1); // Simpan nomor baris yang duplikat
//                 duplicateCount++; // Tambah jumlah duplikat
//             } else {
//                 uniqueSet.add(key);
//             }
//         }

//         // Menyorot baris duplikat
//         var rangeList = duplicateRows.map(row => sheet.getRange(row, 1, 1, sheet.getLastColumn()));
//         rangeList.forEach(range => range.setBackground("green").setFontColor("white"));

//         // Menampilkan hasil di console
//         console.log(`Sheet: ${sheetName}`);
//         console.log(`Total duplikat ditemukan: ${duplicateCount}`);
//         console.log(`Baris duplikat: ${duplicateRows.join(", ")}`);
//     });
// }


// Menyorot duplikat tanpa memperhitungkan "Dr"
function highlightDuplicatesWithoutDr() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheets = ["ALL Dentist"]; // Nama sheet

    sheets.forEach(sheetName => {
        var sheet = ss.getSheetByName(sheetName);
        if (!sheet) return;

        var range = sheet.getDataRange();
        var values = range.getValues();
        var nameCol = 1;  // Kolom Name (B)
        var addressCol = 3;  // Kolom Address (E)
        var postalCodeCol = 4;  // Kolom Postal code (F)
        var cityCol = 5;  // Kolom City (G)

        var uniqueSet = new Set();
        var duplicateRows = [];
        var duplicateCount = 0;

        for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
            if (!values[i][nameCol]) continue;

            // Hilangkan title "Dr " dari nama
            var cleanName = values[i][nameCol].replace(/^Dr\s+/i, "").trim();

            // Buat kunci unik berdasarkan nama tanpa "Dr", kode pos, dan kota
            var key = cleanName + values[i][postalCodeCol] + values[i][cityCol];

            if (uniqueSet.has(key)) {
                duplicateRows.push(i + 1); // Simpan nomor baris yang duplikat
                duplicateCount++; // Tambah jumlah duplikat
            } else {
                uniqueSet.add(key);
            }
        }

        // Menyorot baris duplikat
        var rangeList = duplicateRows.map(row => sheet.getRange(row, 1, 1, sheet.getLastColumn()));
        rangeList.forEach(range => range.setBackground("green").setFontColor("white"));

        // Menampilkan hasil di console
        console.log(`Sheet: ${sheetName}`);
        console.log(`Total duplikat ditemukan: ${duplicateCount}`);
        console.log(`Baris duplikat: ${duplicateRows.join(", ")}`);
    });
}




// // hapus duplicate
// function removeDuplicates() {
//     var ss = SpreadsheetApp.getActiveSpreadsheet();
//     var sheets = ["ALL Dentist"]; // Nama sheet

//     sheets.forEach(sheetName => {
//         var sheet = ss.getSheetByName(sheetName);
//         if (!sheet) return;

//         var range = sheet.getDataRange();
//         var values = range.getValues();
//         var nameCol = 1;  // Kolom Name (B)
//         var addressCol = 3;  // Kolom Address (E)
//         var postal_code = 4;  // Kolom Postal code (F)
//         var city_ = 5;  // Kolom City (G)

//         var uniqueSet = new Set();
//         var duplicateRows = [];

//         for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
//             var key = values[i][nameCol] + values[i][addressCol] + values[i][postal_code] + values[i][city_]; // Gabungan Name + Address
//             if (uniqueSet.has(key)) {
//                 duplicateRows.push(i + 1); // Simpan nomor baris yang duplikat
//             } else {
//                 uniqueSet.add(key);
//             }
//         }

//         // Menghapus baris duplikat dari bawah ke atas agar indeks tidak bergeser
//         duplicateRows.reverse().forEach(row => sheet.deleteRow(row));

//         // Menampilkan hasil di console
//         console.log(`Sheet: ${sheetName}`);
//         console.log(`Total duplikat dihapus: ${duplicateRows.length}`);
//         console.log(`Baris yang dihapus: ${duplicateRows.join(", ")}`);
//     });
// }


// // hapus titk antara title (Dr. Nama) menjadi seperti ini (Dr Nama)
// function removeDotFromTitle() {
//     var ss = SpreadsheetApp.getActiveSpreadsheet();
//     var sheet = ss.getSheetByName("ALL Dentist"); // Ganti dengan nama sheet Anda
//     var nameCol = 2; // Kolom Name (misalnya di kolom A, berarti index = 1)

//     var range = sheet.getRange(2, nameCol, sheet.getLastRow() - 1, 1); // Ambil data mulai dari baris kedua
//     var values = range.getValues();

//     for (var i = 0; i < values.length; i++) {
//         if (values[i][0]) {
//             values[i][0] = values[i][0].replace(/^Dr\.\s*/, "Dr "); // Menghapus titik setelah "Dr."
//         }
//     }

//     range.setValues(values);
//     console.log("Titik setelah 'Dr.' telah dihapus!");
// }





// function splitAddress() {
//     var ss = SpreadsheetApp.getActiveSpreadsheet();
//     var sheet = ss.getSheetByName("Annuaire Améli"); // Ganti dengan nama sheet yang sesuai

//     var range = sheet.getDataRange();
//     var values = range.getValues();
    
//     var addressCol = 3; // Kolom Address (D, index mulai dari 0)
//     var newHeader = ["Business Name", "New Address"];

//     // Tambahkan header baru di kolom E dan F jika belum ada
//     if (values[0].length <= addressCol + 1) {
//         sheet.getRange(1, addressCol + 2, 1, 2).setValues([newHeader]);
//     }

//     for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
//         var address = values[i][addressCol];

//         if (address) {
//             var parts = address.split(",");
//             if (parts.length >= 3) {
//                 var namaKantor = capitalizeWords(parts[0].trim());
//                 var newAddress = capitalizeWords(parts.slice(1).join(",").trim());

//                 sheet.getRange(i + 1, addressCol + 2).setValue(namaKantor); // Kolom E (Nama Kantor)
//                 sheet.getRange(i + 1, addressCol + 3).setValue(newAddress); // Kolom F (New Address)
//             }
//         }
//     }

//     console.log("Pemisahan alamat selesai dengan format huruf besar di awal kata!");
// }

// // Fungsi untuk membuat huruf pertama dari setiap kata menjadi huruf besar
// function capitalizeWords(str) {
//     return str.toLowerCase().replace(/\b\w/g, function(char) {
//         return char.toUpperCase();
//     });
// }


// memsiahkan alamat ke kolom baru

// function splitAddress() {
//     var ss = SpreadsheetApp.getActiveSpreadsheet();
//     var sheet = ss.getSheetByName("Annuaire Améli"); // Ganti dengan nama sheet yang sesuai

//     var range = sheet.getDataRange();
//     var values = range.getValues();
    
//     var addressCol = 3; // Kolom Address (D, index mulai dari 0)
//     var newHeader = ["Business Name", "New Address"];

//     // Tambahkan header baru di kolom E dan F jika belum ada
//     if (values[0].length <= addressCol + 1) {
//         sheet.getRange(1, addressCol + 2, 1, 2).setValues([newHeader]);
//     }

//     for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
//         var address = values[i][addressCol];

//         if (address) {
//             var parts = address.split(",");
//             if (parts.length >= 3) {
//                 // Jika ada 3 bagian (koma), pisahkan nama kantor & alamat
//                 var namaKantor = capitalizeWords(parts[0].trim());
//                 var newAddress = capitalizeWords(parts.slice(1).join(",").trim());

//                 sheet.getRange(i + 1, addressCol + 2).setValue(namaKantor); // Kolom E (Nama Kantor)
//                 sheet.getRange(i + 1, addressCol + 3).setValue(newAddress); // Kolom F (New Address)
//             } else {
//                 // Jika hanya ada 2 bagian, simpan semua di New Address
//                 var newAddress = capitalizeWords(address.trim());
//                 sheet.getRange(i + 1, addressCol + 3).setValue(newAddress); // Kolom F (New Address)
//             }
//         }
//     }

//     console.log("Pemisahan alamat selesai dengan kondisi 2 dan 3 indeks koma!");
// }

// // Fungsi untuk membuat huruf pertama dari setiap kata menjadi huruf besar
// function capitalizeWords(str) {
//     return str.toLowerCase().replace(/\b\w/g, function(char) {
//         return char.toUpperCase();
//     });
// }


// // memisahkan kode pos, city kekolom baru 
// function extractPostalCodeAndCity() {
//     var ss = SpreadsheetApp.getActiveSpreadsheet();
//     var sheet = ss.getSheetByName("ONCD"); // Ganti sesuai nama sheet

//     var range = sheet.getDataRange();
//     var values = range.getValues();

//     var newAddressCol = 3; // Kolom New Address (F, index mulai dari 0)
//     var newHeaders = ["Postal Code", "City"];

//     // Tambahkan header baru di kolom G dan H jika belum ada
//     if (values[0].length <= newAddressCol + 1) {
//         sheet.getRange(1, newAddressCol + 2, 1, 2).setValues([newHeaders]);
//     }

//     for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
//         var newAddress = values[i][newAddressCol];

//         if (newAddress) {
//             var parts = newAddress.split(",");
//             var postalCity = parts[parts.length - 1].trim(); // Ambil bagian terakhir (Kode Pos + Kota)
//             var match = postalCity.match(/(\d{5})\s(.+)/); // Cari pola "12345 Kota"

//             if (match) {
//                 var postalCode = "'" + match[1]; // Tambahkan tanda petik satu di depan kode pos
//                 var city = match[2]; // Ambil nama kota
                
//                 // Hapus Postal Code & City dari New Address
//                 var cleanedAddress = parts.slice(0, parts.length - 1).join(",").trim();

//                 // Simpan ke sheet
//                 sheet.getRange(i + 1, newAddressCol + 2).setValue(postalCode); // Kolom G (Postal Code)
//                 sheet.getRange(i + 1, newAddressCol + 3).setValue(capitalizeWords(city)); // Kolom H (City)
//                 sheet.getRange(i + 1, newAddressCol + 1).setValue(cleanedAddress); // Update New Address (tanpa Postal Code & City)
//             }
//         }
//     }

//     console.log("Postal Code and City extraction complete! New Address has been updated.");
// }

// // Fungsi untuk membuat huruf pertama dari setiap kata menjadi huruf besar
// function capitalizeWords(str) {
//     return str.toLowerCase().replace(/\b\w/g, function(char) {
//         return char.toUpperCase();
//     });
// }




// // kasus kedua sheet ke 1/ pertama
// function extractPostalCodeAndCity() {
//     var ss = SpreadsheetApp.getActiveSpreadsheet();
//     var sheet = ss.getSheetByName("Doctolib"); // Ganti sesuai nama sheet

//     var range = sheet.getDataRange();
//     var values = range.getValues();

//     var addressCol = 4; // Kolom Address (E) (Google Sheets index mulai dari 0)
//     var newHeaders = ["Postal Code", "City"];

//     // Tambahkan header baru di kolom E dan F jika belum ada
//     if (values[0].length <= addressCol + 1) {
//         sheet.getRange(1, addressCol + 2, 1, 2).setValues([newHeaders]);
//     }

//     for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
//         var fullAddress = values[i][addressCol];

//         if (fullAddress) {
//             var parts = fullAddress.split(",");
//             var postalCityPart = parts.slice(-2).join(",").trim(); // Ambil 2 bagian terakhir
//             var match = postalCityPart.match(/(\d{5})/g); // Cari semua kode pos

//             if (match) {
//                 var postalCode = "'" + match[0]; // Ambil kode pos pertama & tambahkan petik satu
//                 var city = capitalizeWords(parts[parts.length - 1].trim()); // Ambil bagian kota
                
//                 // Jika ada dua kode pos, pastikan hanya mengambil yang pertama
//                 if (match.length > 1) {
//                     city = capitalizeWords(parts[parts.length - 1].replace(match[1], "").trim());
//                 }

//                 // Hapus Postal Code dari Address
//                 var cleanedAddress = fullAddress.replace(/\d{5},?\s?/g, "").trim();
                
//                 // Hapus City dari Address (gunakan regex dinamis untuk menghindari kesalahan)
//                 var cityRegex = new RegExp("\\b" + city.replace(/[-']/g, "\\$&") + "\\b", "gi");
//                 cleanedAddress = cleanedAddress.replace(cityRegex, "").trim();
                
//                 // Pastikan tidak ada koma ekstra di akhir
//                 cleanedAddress = cleanedAddress.replace(/,\s*$/, "").trim();

//                 // Simpan ke sheet
//                 sheet.getRange(i + 1, addressCol + 2).setValue(postalCode); // Kolom E (Postal Code)
//                 sheet.getRange(i + 1, addressCol + 3).setValue(city); // Kolom F (City)
//                 sheet.getRange(i + 1, addressCol + 1).setValue(cleanedAddress); // Update Address tanpa Postal Code & City
//             }
//         }
//     }

//     console.log("Ekstraksi Postal Code & City selesai! Address sudah diperbarui.");
// }

// // Fungsi untuk membuat huruf pertama dari setiap kata menjadi huruf besar
// function capitalizeWords(str) {
//     return str.toLowerCase().replace(/\b\w/g, function(char) {
//         return char.toUpperCase();
//     });
// }


// // // kasus ketiga sheet 3
// // function extractPostalCodeAndCity() {
// //     var ss = SpreadsheetApp.getActiveSpreadsheet();
// //     var sheet = ss.getSheetByName("Annuaire dentaire"); // Sesuaikan dengan nama sheet

// //     var range = sheet.getDataRange();
// //     var values = range.getValues();

// //     var addressCol = 4; // Kolom New Address (E) (Google Sheets index mulai dari 0)
// //     var newHeaders = ["Postal Code", "City"];

// //     // Tambahkan header baru jika belum ada
// //     if (values[0].length <= addressCol + 1) {
// //         sheet.getRange(1, addressCol + 2, 1, 2).setValues([newHeaders]);
// //     }

// //     for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
// //         var fullAddress = values[i][addressCol];

// //         if (fullAddress) {
// //             var parts = fullAddress.split(" ");
// //             var postalCode = "";
// //             var city = "";
// //             var cleanedAddress = "";

// //             // Cek apakah ada kode pos (5 digit angka berturut-turut)
// //             for (var j = 0; j < parts.length; j++) {
// //                 if (/^\d{5}$/.test(parts[j])) { // Jika menemukan 5 digit angka
// //                     postalCode = "'" + parts[j]; // Tambahkan petik satu di awal
// //                     city = parts.slice(j + 1).join(" "); // Ambil kata-kata setelah postal code
// //                     cleanedAddress = parts.slice(0, j).join(" "); // Ambil bagian sebelum postal code
// //                     break;
// //                 }
// //             }

// //             // Simpan ke sheet
// //             sheet.getRange(i + 1, addressCol + 2).setValue(postalCode); // Kolom E (Postal Code)
// //             sheet.getRange(i + 1, addressCol + 3).setValue(capitalizeWords(city)); // Kolom F (City)
// //             sheet.getRange(i + 1, addressCol + 1).setValue(cleanedAddress); // Update Address tanpa Postal Code & City
// //         }
// //     }

// //     console.log("Postal Code and City extraction complete! New Address has been updated.");
// // }

// // // Fungsi untuk membuat huruf pertama dari setiap kata menjadi huruf besar
// // function capitalizeWords(str) {
// //     return str.toLowerCase().replace(/\b\w/g, function(char) {
// //         return char.toUpperCase();
// //     });
// // }


// // // kasus ketiga sheet 4
// // function extractPostalCodeAndCity() {
// //     var ss = SpreadsheetApp.getActiveSpreadsheet();
// //     var sheet = ss.getSheetByName("Invisalign"); // Sesuaikan nama sheet

// //     var range = sheet.getDataRange();
// //     var values = range.getValues();

// //     var addressCol = 4; // Kolom New Address (E) (Google Sheets index mulai dari 0)
// //     var newHeaders = ["Postal Code", "City"];

// //     // Tambahkan header baru jika belum ada
// //     if (values[0].length <= addressCol + 1) {
// //         sheet.getRange(1, addressCol + 2, 1, 2).setValues([newHeaders]);
// //     }

// //     for (var i = 1; i < values.length; i++) { // Mulai dari baris kedua (hindari header)
// //         var fullAddress = values[i][addressCol];

// //         if (fullAddress) {
// //             var parts = fullAddress.split(",").map(s => s.trim()); // Pisahkan dengan koma

// //             if (parts.length >= 3) { 
// //                 var postalCode = "'" + parts[1].trim(); // Ambil elemen ke-2 (Kode Pos) + Petik satu
// //                 var city = capitalizeWords(parts[2].replace(/\bFR\b/gi, "").trim()); // Ambil elemen ke-3 (Kota)
// //                 var cleanedAddress = parts[0].trim(); // Bagian sebelum postal code

// //                 // Simpan ke sheet
// //                 sheet.getRange(i + 1, addressCol + 2).setValue(postalCode); // Kolom E (Postal Code)
// //                 sheet.getRange(i + 1, addressCol + 3).setValue(city); // Kolom F (City)
// //                 sheet.getRange(i + 1, addressCol + 1).setValue(cleanedAddress); // Update Address tanpa Postal Code & City
// //             }
// //         }
// //     }

// //     console.log("Postal Code and City extraction complete! New Address has been updated.");
// // }

// // // Fungsi untuk membuat huruf pertama dari setiap kata menjadi huruf besar
// // function capitalizeWords(str) {
// //     return str.toLowerCase().replace(/\b\w/g, function(char) {
// //         return char.toUpperCase();
// //     });
// // }



// // memperbaiki text capital
// function capitalizeEachWord() {
//     var ss = SpreadsheetApp.getActiveSpreadsheet();
//     var sheet = ss.getSheetByName("ALL Dentist"); // Ganti dengan nama sheet yang sesuai
//     var addressCol = 2; // Kolom Address (D = 4)

//     var range = sheet.getRange(2, addressCol, sheet.getLastRow() - 1, 1); // Ambil data mulai dari baris ke-2
//     var values = range.getValues();

//     for (var i = 0; i < values.length; i++) {
//         if (values[i][0]) {
//             values[i][0] = values[i][0].toLowerCase().replace(/\b\w/g, c => c.toUpperCase()); 
//         }
//     }

//     range.setValues(values);
//     console.log("Perbaikan teks selesai!");
// }



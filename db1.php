<?php
// Memeriksa apakah formulir sudah disubmit
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Membuat koneksi ke database
    $koneksi = mysqli_connect("localhost", "username", "password", "regis");

    // Memeriksa koneksi
    if (!$koneksi) {
        die("Koneksi ke database gagal: " . mysqli_connect_error());
    }

    // Menangkap data dari formulir
    $nama = $_POST['nama'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Menyimpan data ke dalam database
    $query = "INSERT INTO users (nama, email, password) VALUES ('$nama', '$email', '$password')";
    if (mysqli_query($koneksi, $query)) {
        echo "Pendaftaran berhasil!";
    } else {
        echo "Error: " . $query . "<br>" . mysqli_error($koneksi);
    }

    // Menutup koneksi
    mysqli_close($koneksi);
}
?>

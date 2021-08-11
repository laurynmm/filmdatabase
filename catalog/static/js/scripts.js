function fillReviewForm(id) {
    document.getElementById('id_film').value = id;
    document.getElementById('id_date_watched').value = new Date().toISOString().substr(0, 10);
    document.getElementById('reviewform').submit();
}
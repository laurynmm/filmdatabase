function showCreateForm(button, id_film, id_form) {
    let form = document.getElementById(id_form);
    let film = button.parentElement;
    document.getElementById('id_film').value = id_film;

    if (form.parentElement == film)
        return;

    form.style.display = "none";
    form.remove();

    form.style.display = 'block';
    film.insertBefore(form, button.nextSibling);
}

function showEditForm(button, id_review, id_form) {
    let form = document.getElementById(id_form);
    let review = button.parentElement

    if (form.parentElement == review)
        return;

    document.getElementById('id_review').value = id_review;

    form.style.display = "none";
    form.remove();

    form.style.display = 'block';
    review.appendChild(form);
}

function hideForm(formId) {
    let form = document.getElementById(formId);
    form.style.display = 'none';
}
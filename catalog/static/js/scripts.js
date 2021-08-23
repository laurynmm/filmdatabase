// eslint-disable-next-line no-unused-vars
function showCreateForm(button, id_film, id_form) {
    let form = document.getElementById(id_form);
    let film = button.parentElement;
    document.getElementById('id_film').value = id_film;

    if (form.parentElement === film)
        return;

    form.style.display = 'none';
    form.remove();

    form.style.display = 'block';
    film.insertBefore(form, button.nextSibling);
}

// eslint-disable-next-line no-unused-vars
function showEditForm(button, id_review, id_form) {
    let form = document.getElementById(id_form);
    let review = button.parentElement;

    if (form.parentElement === review)
        return;

    document.getElementById('id_review').value = id_review;

    form.style.display = 'none';
    form.remove();

    form.style.display = 'block';
    review.appendChild(form);
}

// eslint-disable-next-line no-unused-vars
function hideForm(formId) {
    let form = document.getElementById(formId);
    form.style.display = 'none';
}

// eslint-disable-next-line no-unused-vars
function searchBox(id, urlData) {
    window.addEventListener('load', () => {
    // eslint-disable-next-line no-undef
        new TomSelect(id, {
            maxItems: 1,
            maxOptions: 100,
            valueField: 'id',
            labelField: 'title',
            searchField: 'title',
            sortField: 'title',
            create: false,
            load: function (query, callback) {
                var url = `${urlData}?q=${encodeURIComponent(query)}`;
                fetch(url)
                    .then(response => response.json())
                    .then(json => {
                        callback(json);
                    }).catch(() => {
                        callback();
                    });
            },
            render: {
                option: function (data, escape) {
                    return `<div>${escape(data.title)} (${escape(data.year)})</div>`;
                },
                item: function (data, escape) {
                    return `<div>${escape(data.title)} (${escape(data.year)})</div>`;
                }
            }
        });
    });
}

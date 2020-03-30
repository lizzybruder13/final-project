"use strict."

$(function() {
    $('#viewAllEvents').on('click', showAllEvents);

    function flashMessage (evt) {

        alert("Working");
    }

    function showAllEvents (evt) {

        evt.preventDefault();

        $('#searchDisplay').hide();
    
        $.get('/all_events', (res) => {

            $('#body').empty()

            for (event of res) {
                $('#body').append(
                    `<a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">${event.type} - ${event.location}</h5>
                    </div>
                    <p class="mb-1">${event.weekday} at ${event.time}</p>
                    </a>`
                );
            }
        });
    }

})


$(function() {
    $('#viewAllLocations').on('click', showAllLocations);

    function showAllLocations (evt) {

        evt.preventDefault();

        $('#searchDisplay').hide();
    
        $.get('/all_locations', (res) => {

            $('#body').empty()

            for (loc of res) {
                $('#body').append(
                    `<a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">${loc.name}</h5>
                    </div>
                    <p class="mb-1">${loc.address}</p>
                    <p class="mb-1">${loc.city}, MN ${loc.zipcode}</p>
                    </a>`
                );
            }
        });
    }

})


$(function() {
    $('#viewAllEventTypes').on('click', showAllEventTypes);

    function showAllEventTypes (evt) {

        evt.preventDefault();

        $('#searchDisplay').hide();
    
        $.get('/all_event_types', (res) => {

            $('#body').empty()

            for (evt_type of res) {
                $('#body').append(
                    `<button type="button" class="btn btn-lg w-50 btn-info">
                    ${evt_type.name}</button>`
                );
            }
        });
    }

})


$(function() {
    $('#searchForm').on('click', displayForm);

    function displayForm (evt) {

        evt.preventDefault();

        $('#body').empty()

        $('#searchDisplay').show();

    };
    
})

$(function() {
    $('#searchResult').on('click', displayResults);

    function displayResults (evt) {

        evt.preventDefault();

        $('#searchDisplay').hide();

        data = $('form').serialize();
    
        $.get('/search_results', data, (res) => {

            $('#body').empty()

            console.log(res)

            for (result of res) {

                $('#body').append(
                    `<a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">${result.type} - ${result.location}</h5>
                    </div>
                    <p class="mb-1">${result.weekday} at ${result.time}</p>
                    </a>`
                );
            }
        });

    };
    
})


$(function() {
    $('#goHome').on('click', displayFeatured);

    function displayFeatured (evt) {

        evt.preventDefault();

        $('#searchDisplay').hide();
    
        $.get('/featured_events', (res) => {

            $('#body').empty()

            for (feat_evt of res) {

                $('#body').append(
                    `<a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">${feat_evt.type} - ${feat_evt.location}</h5>
                    </div>
                    <p class="mb-1">${feat_evt.weekday} at ${feat_evt.time}</p>
                    </a>`
                );
            }
        });

    };
    
})
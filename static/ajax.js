"use strict."

function displayMoreEventInfo (event_id, location_id) {

    $('#searchDisplay').hide();

    data = {'event_id': event_id, 'location_id': location_id}

    $.get('/more_event_info', data, (res) => {

        $('#pageHeader').empty();

        $('#body').empty();

        $('#body').append(
                `<h1>${res[0].type} - ${res[0].location}</h1><br>
                <h2>${res[0].weekday} at ${res[0].time}</h2><br>
                <h3>${res[0].address} ${res[0].city}, MN ${res[0].zipcode}</h3><br>
                <h1>Other events at ${res[0].location}:</h1><br>
                `
            );

        event_list = res[1];

        for (event of event_list) {

            $('#body').append(
                `<button type='button' class="list-group-item list-group-item-action" 
                onclick="displayMoreEventInfo(${event.event_id}, ${event.location_id})">
                <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">${event.type} - ${event.weekday} at ${event.time}</h5>
                </div>
                </button>`
            );
        }
    });

}

$(function() {
    $('#viewAllEvents').on('click', showAllEvents);

    function showAllEvents (evt) {

        evt.preventDefault();

        $('#searchDisplay').hide();
    
        $.get('/all_events', (res) => {

            $('#pageHeader').empty();

            $('#pageHeader').append('All Events');

            $('#body').empty();

            for (event of res) {
                $('#body').append(
                    `<button type='button' class="list-group-item list-group-item-action" 
                    onclick="displayMoreEventInfo(${event.event_id}, ${event.location_id})">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">${event.type} - ${event.location}</h5>
                    </div>
                    <p class="mb-1">${event.weekday} at ${event.time}</p>
                    <p class="mb-1">${event.city}</p>
                    </button>`
                );
            }
        });
    }

})

function displayMoreLocInfo (location_id) {

    $('#searchDisplay').hide();

    data = {'location_id': location_id}

    $.get('/more_loc_info', data, (res) => {

        $('#pageHeader').empty();

        $('#body').empty();

        console.log(res)

        $('#body').append(
                `<h1>${res[0].name}</h1><br>
                <h2>${res[0].address} ${res[0].city}, MN ${res[0].zipcode}</h2><br>
                <h1>Events:</h1><br>
                `
            );

        event_list = res[1];

        for (event of event_list) {

            $('#body').append(
                `<button type='button' class="list-group-item list-group-item-action" 
                onclick="displayMoreEventInfo(${event.event_id}, ${event.location_id})">
                <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">${event.type} - ${event.weekday} at ${event.time}</h5>
                </div>
                </button>`
            );
        }
    });

}


$(function() {
    $('#viewAllLocations').on('click', showAllLocations);

    function showAllLocations (evt) {

        evt.preventDefault();

        $('#searchDisplay').hide();
    
        $.get('/all_locations', (res) => {

            $('#pageHeader').empty();

            $('#pageHeader').append('All Locations');

            $('#body').empty()

            for (loc of res) {
                $('#body').append(
                    `<button type='button' class="list-group-item list-group-item-action"
                    onclick="displayMoreLocInfo(${loc.location_id})">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">${loc.name}</h5>
                    </div>
                    <p class="mb-1">${loc.address}</p>
                    <p class="mb-1">${loc.city}, MN ${loc.zipcode}</p>
                    </button>`
                );
            }
        });
    }

})

function displayTypeResults (type_id) {

    $('#searchDisplay').hide();

    data = {'type_id': type_id}

    $.get('/search_results', data, (res) => {

        $('#pageHeader').empty();

        $('#pageHeader').append(`All Bingo Events`);

        $('#body').empty()

        for (event of res) {

            $('#body').append(
                `<a href="#" class="list-group-item list-group-item-action">
                <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">${event.type} - ${event.location}</h5>
                </div>
                <p class="mb-1">${event.weekday} at ${event.time}</p>
                <p class="mb-1">${event.city}</p>
                </a>`
            );
        }
    });

}

$(function() {
    $('#viewAllEventTypes').on('click', showAllEventTypes);

    function showAllEventTypes (evt) {

        evt.preventDefault();

        $('#searchDisplay').hide();
    
        $.get('/all_event_types', (res) => {

            $('#pageHeader').empty();

            $('#body').empty()

            $('#body').append(`<form id='eventTypes' action='/search_results'></form>`);

            for (evt_type of res) {
                $('#eventTypes').append(
                    `<button type="button" 
                    onclick="displayTypeResults(${evt_type.type_id})"
                    class="btn btn-lg w-50 btn-info">
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

        $('#pageHeader').empty();

        $('#pageHeader').append('Search:');

        $('#body').empty()

        $('#searchDisplay').show();

    };
    
})

$(function() {
    $('#searchResult').on('click', displayResults);

    function displayResults (evt) {

        evt.preventDefault();

        $('#searchDisplay').hide();

        data = $('#customSearch').serialize();
    
        $.get('/search_results', data, (res) => {

            var i = 0;

            for (result of res) {

                i++;

            }

            $('#pageHeader').empty();

            $('#pageHeader').append(`${i} Results Found:`);

            $('#body').empty()

            for (result of res) {

                $('#body').append(
                    `<a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">${result.type} - ${result.location}</h5>
                    </div>
                    <p class="mb-1">${result.weekday} at ${result.time}</p>
                    <p class="mb-1">${result.city}</p>
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

            $('#pageHeader').empty();

            $('#pageHeader').append('Featured Events');

            $('#body').empty()

            for (feat_evt of res) {

                $('#body').append(
                    `<a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">${feat_evt.type} - ${feat_evt.location}</h5>
                    </div>
                    <p class="mb-1">${feat_evt.weekday} at ${feat_evt.time}</p>
                    <p class="mb-1">${feat_evt.city}</p>
                    </a>`
                );
            }
        });

    };
    
})

function saveData() {

    data = $('#body')

    $.Storage.set(`${i}`, `${data}`);

    i++;

};

function getBackData() {

    current = current - 1;

    if (back != 0) {

        back = i-1;

        data = $.Storage.get(`${back}`);

        $('#body').empty();

        $('#body').append(data);

    }

}

function getForwardData() {


}
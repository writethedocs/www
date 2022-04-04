$(document).ready(function() {
    // This is a CF account Eric controls
    var feed = "https://cors.writethedocs.workers.dev/corsproxy/?apiurl=https://jobs.writethedocs.org/feeds/rss.xml";

    $.get(feed)
    .always(
        function(data) {
            console.log('Got data')
            var list = $("#jobs-listing").find('ul');

            console.log('Got list')

            // Create HTML
            $(data).find("item").each(function () {
                var el = $(this);
                var title = el.find("title").text();
                var link =  el.find("link").text();
                var description =  el.find("description").text();
                var data = description.split('\n', 3)
                var location = data[1].trim()
                var company = data[2].trim().replace('<br/>', '')
                var fulltitle = company + ' - ' + title
                var li = $('<li/>')
                    .appendTo(list);
                var aaa = $('<a/>')
                    .text(fulltitle)
                    .attr('href',link)
                    .appendTo(li);
                console.log('Got link')
            });
            console.log(list)
        }
    )
});

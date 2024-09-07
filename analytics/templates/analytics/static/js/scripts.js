document.addEventListener('DOMContentLoaded', function() {
    const platformFilter = document.getElementById('platformFilter');
    const postsTable = document.getElementById('postsTable');

    platformFilter.addEventListener('change', function() {
        const selectedPlatform = platformFilter.value;
        const rows = postsTable.querySelectorAll('tr');

        rows.forEach(row => {
            if (selectedPlatform === 'all' || row.dataset.platform === selectedPlatform) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
});

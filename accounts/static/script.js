function fetchStatement() {
    const iban = document.getElementById('statement-iban').value;
    const url = iban ? `/statement/?iban=${iban}` : '/statement/';
    fetch(url)
        .then(response => response.json())
        .then(data => updateStatement(data.transactions))
        .catch(error => console.error('Error fetching statement:', error));
}

function displayResult(message) {
    document.getElementById('result-container').textContent = message;
}

function updateStatement(transactions) {
    let statementHtml = '<table><tr><th>Date</th><th>Type</th><th>Amount</th><th>Balance</th></tr>';
    transactions.forEach(tx => {
        statementHtml += `<tr><td>${tx.date}</td><td>${tx.transaction_type}</td><td>${tx.amount}</td><td>${tx.balance}</td></tr>`;
    });
    statementHtml += '</table>';
    document.getElementById('statement-container').innerHTML = statementHtml;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

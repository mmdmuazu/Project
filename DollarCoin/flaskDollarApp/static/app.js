function showcontent(id) {
    const contents = document.querySelectorAll('.content');
    contents.forEach(content => content.classList.remove('active'));
    document.getElementById(id).classList.add('active');
}
function copyaddress(){
    // Get the text field
    var copyText = document.getElementById("input-address");

    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices
    
        // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);
    var copyaddress = document.getElementById('copy-address');
    copyaddress.innerHTML = 'Copied';
    setTimeout(() => {
        copyaddress.innerHTML = 'copy';
    },1000)
    }

function copy() {
    // Get the text field
    var copyText = document.getElementById("input");

    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices

    // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);
    document.getElementById('copy').innerHTML = 'Copied';
    setTimeout(()=>{
        document.getElementById('copy').innerHTML = 'copy';   
    },1000)
}
function claim(){
    sessionStorage.removeItem('cb_items_store');
    location.reload(); 
    document.getElementById("claim").innerHTML="claimed"
  };

document.addEventListener('DOMContentLoaded', () => {
    const dailyTaskLink = document.getElementById('daily-task-link');
    const lastClickKey = 'dailyTaskLastClick';
    const coinsEarned = parseFloat(dailyTaskLink.getAttribute('data-coins'));
    let balance = 0; // Initialize balance
    const balanceElement = document.getElementById('balance');
    
    // Function to update the balance on the server
    function updateBalanceOnServer(amount) {
        fetch('/update_balance', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ amount: amount }) // Send the amount to the server
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error(data.error);
            } else {
                balance = data.balance;
                balanceElement.textContent = `Counting ${balance} Coins`;
            }
        })
        .catch(error => console.error('Error:', error));
    }
    console.log(updateBalanceOnServer)

    // Function to fetch and update the link states
    function fetchLinkStates() {
        fetch('/get_link_states')
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error(data.error);
                } else {
                    data.links.forEach(link => {
                        const taskLink = document.querySelector(`a[href="${link.href}"]`);
                        if (taskLink) {
                            if (link.used) {
                                taskLink.classList.add('used');
                                taskLink.style.pointerEvents = 'none';
                                taskLink.style.opacity = '0.5';
                                
                            }
                        }
                    });
                }
            })
            .catch(error => console.error('Error:', error));
    }

    // Function to update the state of the daily task link
    function updateDailyTaskLinkState() {
        const lastClickTime = localStorage.getItem(lastClickKey);
        if (lastClickTime) {
            const now = Date.now();
            const timeDiff = now - lastClickTime;
            const twentyFourHours = 24 * 60 * 60 * 1000; // 24 hours in milliseconds

            if (timeDiff < twentyFourHours) {
                dailyTaskLink.style.pointerEvents = 'none';
                dailyTaskLink.style.opacity = '0.5';
                return;
            }
        }
        dailyTaskLink.style.pointerEvents = 'auto';
        dailyTaskLink.style.opacity = '1.0';
    }

    // Event listener for the daily task link
    dailyTaskLink.addEventListener('click', (event) => {
        if (dailyTaskLink.style.pointerEvents !== 'none') {
            event.preventDefault(); // Prevent default link behavior

            // Update last click time
            localStorage.setItem(lastClickKey, Date.now());

            // Update the balance on the server
            updateBalanceOnServer(coinsEarned);

            // Disable the link after clicking
            dailyTaskLink.style.pointerEvents = 'none';
            dailyTaskLink.style.opacity = '0.5';

            // Open the link in a new tab after a slight delay
            setTimeout(() => {
                window.open(dailyTaskLink.href, '_blank'); // Open in new tab
            }, 200);
        }
    });

    // Update link state on page load
    updateDailyTaskLinkState();
    fetchLinkStates(); // Fetch and update the state of task links

    // Add click event listener to the mining area
    const miningArea = document.getElementById('mining-area');
    miningArea.addEventListener('click', () => {
        miningArea.classList.add('clicked');
        const amountToAdd = 1; // Define the amount to add
        updateBalanceOnServer(amountToAdd); // Update the balance on the server
        setTimeout(() => {
            miningArea.classList.remove('clicked');
        }, 200); // Duration of the animation
    });

    // Add click event listeners to task links in the task box
    const taskLinks = document.querySelectorAll('#task-box a');
    taskLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            // Prevent the default link behavior
            event.preventDefault();

            // Check if the link has been used before
            if (!link.classList.contains('used')) {
                // Mark the link as used on the server
                fetch('/mark_link_used', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ href: link.href })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        console.error(data.error);
                    } else {
                        // Update link state and balance
                        link.classList.add('used');
                        link.style.pointerEvents = 'none';
                        link.style.opacity = '0.5';
                        link.style.textDecoration = 'line-through';

                        const coins = parseFloat(link.getAttribute('data-coins'));
                        if (!isNaN(coins)) {
                            balance += coins;
                            balanceElement.textContent = `Counting ${balance.toFixed(1)} Coins`;
                            updateBalanceOnServer(coins); // Update the balance on the server
                        } else {
                            console.error('Invalid coin value');
                        }

                        // Open the link in a new tab
                        window.open(link.href, '_blank'); // Open in new tab
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        });
    });

    // Handle form submission
    const form = document.getElementById('transfer-form');
    const alertBox = document.getElementById('alert-box');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(form);
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            alertBox.textContent = result.message;
            alertBox.className = 'alert success show'; // Apply success style
        } else {
            alertBox.textContent = result.message;
            alertBox.className = 'alert error show'; // Apply error style
        }
        alertBox.style.display = 'block'; // Show the alert box

        // Hide alert after 5 seconds
        setTimeout(() => {
            alertBox.style.display = 'none';
            alertBox.className = 'alert'; // Remove the show class
        }, 5000);

        form.reset(); // Optionally, reset the form
    });
});
document.getElementById('mining-area').addEventListener('click', function(event) {
    const popup = document.createElement('div');
    popup.classList.add('popup');
    popup.innerText = '+1';
    // Position the popup at the click location
    const rect = this.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    popup.style.left = `${x}px`;
    popup.style.top = `${y}px`;
    popup.style.fontSize = "50px";

    this.appendChild(popup);

    // Animate the popup
    setTimeout(() => {
        popup.classList.add('flying');
    }, 0);

    // Remove the popup after animation
    popup.addEventListener('transitionend', () => {
        popup.remove();
    });
});
const airtime_footer = document.getElementById('airtime-footer');
const airtime_message = document.getElementById('airtime-message')
const airtime_menu = document.getElementById('airtime-menu');
const airtime_form = document.getElementById('airtime-form');

airtime_form.addEventListener('submit',(event)=>{
    event.preventDefault();
    const phone_number = document.getElementById('phone-number').value;
    const airtime_amount = document.getElementById('airtime-amount').value;

    fetch('/airtime',{
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body : JSON.stringify({phone_number:phone_number,airtime_amount:airtime_amount})

    })
    .then(response => response.json())
    .then(data  => {
        airtime_message.style.display = 'block';
        if (data.error){
            airtime_message.style.backgroundColor = 'red';
            airtime_message.textContent = data.message;
        }
        else {
            airtime_message.style.backgroundColor = 'green';
            airtime_message.textContent = data.message;
        }
        setTimeout(() =>{
            airtime_message.style.display = 'none';
        },2000)
        
    })


})
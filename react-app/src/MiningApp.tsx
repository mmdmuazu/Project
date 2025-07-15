import "./App.css";
import coin from "./assets/coin.png";

function showContent(id: string): void {
  const contents = document.querySelectorAll<HTMLElement>(".content");
  contents.forEach((content) => content.classList.remove("active"));

  const element = document.getElementById(id);
  if (element) {
    element.classList.add("active");
  }
}
const balanceElement = document.getElementById("balance");
// Function to update the balance on the server
function updateBalanceOnServer(amount: any) {
  fetch("http://127.0.0.1:5000/update_balance", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ amount: amount }), // Send the amount to the server
  })
    .then((response) => response.json())
    .then((data) => {
      if (data) {
        if (data.error) {
          console.error(data.error);
        } else {
          const balance = data.balance;
          if (balanceElement) {
            balanceElement.textContent = `Counting ${balance} Coins`;
          }
        }
      }
    })
    .catch((error) => console.error("Error:", error));
}
// Add click event listener to the mining area
const miningArea = document.getElementById("mining-area");
if (miningArea) {
  miningArea.addEventListener("click", () => {
    miningArea.classList.add("clicked");
    const amountToAdd = 1; // Define the amount to add
    updateBalanceOnServer(amountToAdd); // Update the balance on the server
    setTimeout(() => {
      miningArea.classList.remove("clicked");
    }, 200); // Duration of the animation
  });
}

const MiningApp: React.FC = () => {
  return (
    <>
      <div id="app">
        <div className="active content" id="mining">
          <header>
            {/* <i id="transfereble-balance">balance: sbalance</i> */}
            <h1>username</h1>
            <h1>
              <img className="balance-coin" src={coin} alt="coin" /> balance
              Coins
            </h1>
          </header>

          <main className="mine">
            <div id="mining-area">
              <img src={coin} alt="Dollar Coin" />
            </div>
          </main>

          <div className="claim">
            <p>
              <label id="balance">balance claimed</label>
              <button type="button" id="claim">
                Claim
              </button>
            </p>
          </div>
        </div>

        <div className="content" id="task-menu">
          <section className="task header">
            <img className="task-img" src={coin} alt="Dollar Coin" />
            <h1 id="Coins">Earn More Coins</h1>
          </section>

          <section id="daily-box">
            <h1>Daily Tasks</h1>
            <a
              id="daily-task-link"
              href="https://www.highratecpm.com/bhpn1i9v8?key=784f1ce97f50612dbf236c5d6becd22c"
              data-coins="500"
              target="_blank"
              rel="noopener noreferrer"
            >
              <img className="task-icon" src={coin} alt="Dollar Coin" />
              <i>
                {" "}
                Watch And Earn
                <img
                  className="telegram2"
                  src={coin}
                  alt="Dollar Coin"
                /> +500{" "}
              </i>
            </a>
          </section>

          <section id="task-box">
            <h1>Tasks</h1>
            <a href="https://t.me/dollar_coin_channel" data-coins="2000">
              <img className="task-icon" src={coin} alt="Dollar Coin" />
              <i>
                Join our Telegram channel
                <img
                  className="telegram2"
                  src={coin}
                  alt="Dollar Coin"
                /> +2000{" "}
              </i>
            </a>

            <a
              href="https://www.highratecpm.com/xy2z2c5ap7?key=ea57c422e75afb4961248c80d68d281d"
              data-coins="1000"
              target="_blank"
              rel="noopener noreferrer"
            >
              <img className="task-icon" src={coin} alt="Dollar Coin" />
              <i>
                {" "}
                Watch And Earn
                <img
                  className="telegram2"
                  src={coin}
                  alt="Dollar Coin"
                /> +1000{" "}
              </i>
            </a>

            <a
              href="https://x.com/Dollarcoin32536?t=Gt4UETs7z0mmJppG6-rVLQ&s=09"
              data-coins="2000"
            >
              <img className="task-icon" src={coin} alt="twitter icon" />
              <i>
                Follow our X account
                <img
                  className="telegram2"
                  src={coin}
                  alt="Dollar Coin"
                /> +2000{" "}
              </i>
            </a>
          </section>
        </div>

        <div className="content" id="invite">
          <section style={{ borderRadius: "5px" }} className="referral">
            <p>Share this link with your friends to earn rewards:</p>
            <input
              id="input"
              type="text"
              value="{{ referral_link }}"
              readOnly
            />
            <br />
            <button type="button" id="copy">
              Copy
            </button>
          </section>
          <h3>Referred users</h3>
          <ul>{/* Map referred users here dynamically in React */}</ul>
          <br />
        </div>

        <div className="content" id="transfer">
          <img className="task-img" src={coin} alt="Dollar Coin" />
          <br />
          <h3>Balance: sbalance</h3>
          <h5>
            <span style={{ color: "red", fontSize: "large" }}>Notice:</span>
            <span>
              {" "}
              you can only transfer your dollar coins to an existing user before
              launching
            </span>
          </h5>
          <input
            title="your address"
            id="input-address"
            type="text"
            value="{{ dashboard_address }}"
            readOnly
          />
          <button id="copy-address">Copy</button>
          <br />
          <form
            action="{{ url_for('transfer') }}"
            method="post"
            id="transfer-form"
          >
            <div id="alert-box" className="alert"></div>
            <input
              type="text"
              name="recipient_address"
              placeholder="Recipient Address"
              required
            />
            <br />
            <input type="number" name="amount" placeholder="Amount" required />
            <br />
            <input type="submit" id="submit" value="Send" />
          </form>
        </div>

        <footer className="footer-menu">
          <a className="footer-item" onClick={() => showContent("mining")}>
            Mining
          </a>
          <a className="footer-item" onClick={() => showContent("task-menu")}>
            Task
          </a>
          <a className="footer-item" onClick={() => showContent("invite")}>
            Invite
          </a>
          <a className="footer-item" onClick={() => showContent("transfer")}>
            Transfer
          </a>
        </footer>
      </div>
    </>
  );
};

export default MiningApp;

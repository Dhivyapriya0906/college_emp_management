// ===============================
// Employee Bar Chart
// ===============================

const employeeCanvas = document.getElementById("employeeChart");

if (employeeCanvas) {
    new Chart(employeeCanvas, {
        type: "bar",
        data: {
            labels: ["IT", "HR", "Admin", "Accounts"],
            datasets: [{
                label: "Employees",
                data: [15, 8, 5, 7],
                backgroundColor: [
                    "#1E3A8A",
                    "#2563EB",
                    "#3B82F6",
                    "#60A5FA"
                ],
                borderColor: "#1E3A8A",
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true
                },
                title: {
                    display: true,
                    text: "Employees by Department"
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}


// ===============================
// Leave Status Pie Chart
// ===============================

const leaveCanvas = document.getElementById("leaveChart");

if (leaveCanvas) {
    new Chart(leaveCanvas, {
        type: "pie",
        data: {
            labels: [
                "Approved",
                "Pending",
                "Rejected"
            ],
            datasets: [{
                data: [10, 3, 2],
                backgroundColor: [
                    "#16A34A",
                    "#F59E0B",
                    "#DC2626"
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: "Leave Status"
                },
                legend: {
                    position: "bottom"
                }
            }
        }
    });
}
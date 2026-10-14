const searchInput = document.getElementById("student-search");
const departmentFilter = document.getElementById("department-filter");
const statusFilter = document.getElementById("status-filter");
const studentRows = Array.from(document.querySelectorAll("#student-rows tr[data-name]"));
const resultCount = document.getElementById("result-count");
const emptyRow = document.getElementById("empty-row");

function filterStudents() {
  const query = searchInput.value.trim().toLowerCase();
  const department = departmentFilter.value;
  const status = statusFilter.value;
  let visibleCount = 0;

  for (const row of studentRows) {
    const matchesSearch = row.dataset.name.includes(query) || row.dataset.id.includes(query);
    const matchesDepartment = !department || row.dataset.department === department;
    const matchesStatus = !status || row.dataset.status === status;
    const isVisible = matchesSearch && matchesDepartment && matchesStatus;
    row.hidden = !isVisible;
    if (isVisible) visibleCount += 1;
  }

  emptyRow.hidden = visibleCount > 0;
  resultCount.textContent = `${visibleCount} ${visibleCount === 1 ? "student" : "students"}`;
}

searchInput.addEventListener("input", filterStudents);
departmentFilter.addEventListener("change", filterStudents);
statusFilter.addEventListener("change", filterStudents);

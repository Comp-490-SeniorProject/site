import {Component, OnInit} from "@angular/core"
import {ApisService} from "src/app/apis/apis.service"

@Component({
    selector: "app-notifications",
    templateUrl: "./notifications.component.html",
    styleUrls: ["./notifications.component.scss"],
})
export class NotificationsComponent implements OnInit {
    constructor(private apiservice: ApisService) {}

    ngOnInit(): void {
        this.fetchTest()
    }

    status: any

    addNotification(data: any) {
        this.apiservice.createNotification(data).subscribe(
            (res: any) => {
                if (res.status == 200) {
                    let notification = document.getElementById("notification")
                    notification?.classList.remove("d-none")
                } else {
                    this.errorDisplay()
                    this.status = res.statusText
                }
            },
            (error) => {
                this.errorDisplay()
                this.status = error.statusText
            }
        )
    }

    errorDisplay() {
        let input = document.getElementsByTagName("input")
        for (let i = 0; i < input.length; i++) {
            input[i].setAttribute("class", "error form-control")
        }
        let sel = document.getElementsByTagName("select")
        for (let i = 0; i < sel.length; i++) {
            sel[i].setAttribute("class", "error form-control")
        }
    }

    tests = []
    fetchTest() {
        this.apiservice.allTests().subscribe((res: any) => {
            this.tests = res
        })
    }
}

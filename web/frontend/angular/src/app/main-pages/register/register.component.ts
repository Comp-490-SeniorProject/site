import {Component, OnInit} from "@angular/core"
import {FormGroup} from "@angular/forms"
import {Validators} from "@angular/forms"
import {FormBuilder} from "@angular/forms"
import {Router} from "@angular/router"
import {AuthService} from "src/app/auth/auth.service"

@Component({
    selector: "app-register",
    templateUrl: "./register.component.html",
    styleUrls: ["./register.component.scss"],
})
export class RegisterComponent implements OnInit {
    constructor(
        private authService: AuthService,
        private router: Router,
        private formBuilder: FormBuilder
    ) {}

    authForm!: FormGroup
    isSubmitted = false

    ngOnInit() {
        this.authForm = this.formBuilder.group({
            username: ["", Validators.required],
            email: [""],
            password: ["", Validators.required],
            password_confirm: ["", Validators.required],
        })
    }

    get formControls() {
        return this.authForm.controls
    }

    register() {
        this.isSubmitted = true
        if (this.authForm.invalid) {
            return
        }
        this.authService.register(this.authForm.value).subscribe(
            (res: any) => {
                console.log(res)
                this.router.navigateByUrl("homepage")
            },
            (error) => {
                console.log(error)
                let input = document.getElementsByTagName("input")
                for (let i = 0; i < input.length - 1; i++) {
                    input[i].setAttribute("class", "error form-control")
                }
                let err = document.getElementById("error")
                err?.classList.remove("d-none")
            }
        )
    }
}

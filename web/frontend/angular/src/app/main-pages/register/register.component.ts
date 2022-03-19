import {Component, OnInit} from "@angular/core"
import {FormGroup} from "@angular/forms"
import {Validators} from "@angular/forms"
import {FormBuilder} from "@angular/forms"
import {Router} from "@angular/router"
import {AuthService} from "src/app/auth/auth.service"
import * as $ from "jquery"

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
                $("input[type=email],input[type=password]").addClass("error")
                $("#error").removeClass("d-none")
                setTimeout(() => {
                    $("input").removeClass("error")
                    $("#error").addClass("d-none")
                }, 2000)
            }
        )
    }
}

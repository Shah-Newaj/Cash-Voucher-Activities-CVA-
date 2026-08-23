// This script is designed to test the performance of the CVA page traverse functionality of the application.
// It simulates user interactions with the login page, beneficiary list, and beneficiary approval pages,
// measuring response times and ensuring that the pages load successfully under varying load conditions.
// IDE: Visual Studio Code, Command: k6 run .\CVA_Page_Traverse.js

import http from 'k6/http'
import { sleep, check, group } from 'k6'
import { htmlReport } from "https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js";

const BASE_URL = __ENV.BASE_URL || 'https://cashapp.savethechildren.net/'

// Login credentials
const USERNAME = 'SuperAdmin'
const PASSWORD = 'Welcome@2'

// Stress Testing Scenario
export const options = {
    stages: [
        { duration: '1m', target: 50 },
        { duration: '1m', target: 100 },
        { duration: '1m', target: 200 },
        { duration: '1m', target: 300 },
        { duration: '1m', target: 400 },
        { duration: '1m', target: 500 },
        { duration: '5m', target: 500 },
        { duration: '1m', target: 0 }

        // { duration: '1m', target: 50 },
        // { duration: '1m', target: 100 },
        // { duration: '1m', target: 150 },
        // { duration: '1m', target: 200 },
        // { duration: '5m', target: 200 },
        // { duration: '1m', target: 0 }


    ],

    thresholds: {
        http_req_duration: ['p(95)<500'],
    },
}


export default function () {

    group('Login', () => {

        // Open Login Page
        const loginPage = http.get(BASE_URL);

        check(loginPage, {
            'Login Page Loaded': (r) => r.status === 200,
        });


        // Login
        const loginResponse = http.post(
            `${BASE_URL}/Account/Login`,
            {
                ReturnUrl: '/',
                Email: USERNAME,
                Password: PASSWORD,
            },
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            }
        );


        check(loginResponse, {
            [`Login Response | ${loginResponse.status} | ${loginResponse.status_text}`]: (r) => {
                return r.status === 200;
            },
        });


    });

    sleep(1);


    group('Open Beneficiary List Overview', () => {

        const response = http.get(
            `${BASE_URL}/BeneficiaryListOverView`
        );


        check(response, {
            [`Beneficiary List OverView Response | ${response.status} | ${response.status_text}`]: (r) => {
                return r.status === 200;
            },
        });

    });

    sleep(1);


    group('Open Beneficiary List Approval', () => {

        const response = http.get(
            `${BASE_URL}/BeneficiaryListApproval`
        );


        check(response, {
            [`Beneficiary List Approval Response | ${response.status} | ${response.status_text}`]: (r) => {
                return r.status === 200;
            },
        });

    });

    sleep(1);

    group('Open Payment List Overview', () => {

        const response = http.get(
            `${BASE_URL}/PaymentListOverView`
        );


        check(response, {
            [`Payment List OverView Response | ${response.status} | ${response.status_text}`]: (r) => {
                return r.status === 200;
            },
        });

    });

    sleep(1);


    group('Open Payment List Approval', () => {

        const response = http.get(
            `${BASE_URL}/PaymentListApproval`
        );


        check(response, {
            [`Payment List Approval Response | ${response.status} | ${response.status_text}`]: (r) => {
                return r.status === 200;
            },
        });

    });

    sleep(1);

    group('Open Payment Tracking Overview', () => {

        const response = http.get(
            `${BASE_URL}/PaymentTrackingOverview`
        );

        check(response, {
            [`Payment Tracking Response | ${response.status} | ${response.status_text}`]: (r) => {
                return r.status === 200;
            },
        });

    });

    sleep(1);

    group('Open Sample Report Overview', () => {

        const response = http.get(
            `${BASE_URL}/SampleReportOverView`
        );

        check(response, {
            [`Sample Report OverView Response | ${response.status} | ${response.status_text}`]: (r) => {
                return r.status === 200;
            },
        });

    });

    sleep(1);


    group('Open Sample Report Approval', () => {

        const response = http.get(
            `${BASE_URL}/SampleReportApproval`
        );

        check(response, {
            [`Sample Report Approval Response | ${response.status} | ${response.status_text}`]: (r) => {
                return r.status === 200;
            },
        });

    });

    sleep(1);
}


export function handleSummary(data) {
    return {
        "cva_page_traverse_report.html": htmlReport(data),
    }
}
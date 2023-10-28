import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-journal-entry',
  templateUrl: './journal-entry.component.html',
  styleUrls: ['./journal-entry.component.css'],
  standalone: true
})

export class JournalEntryComponent {
  constructor(private router : Router) {}

  navigateTo(route: string) {
    this.router.navigate([route]);
  }
}
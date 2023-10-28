// tabbed-content.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-tabbed-content',
  templateUrl: './tabbed-content.component.html',
  styleUrls: ['./tabbed-content.component.css']
})
export class TabbedContentComponent {
  selectedTab: string = ''; // Initialize as an empty string

  selectTab(tab: string): void {
    this.selectedTab = tab;
  }
}
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';

import { RouterModule } from '@angular/router';
import { CommunityComponent } from './community/community.component';
import { TabbedContentComponent } from './tabbed-content/tabbed-content.component';
import { PhysicalCareComponent } from './physical-care/physical-care.component';
import { MentalHealthComponent } from './mental-health/mental-health.component';
import { PlayerVoiceComponent } from './player-voice/player-voice.component';
import { PhysicalPerformanceComponent } from './physical-performance/physical-performance.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CommunityComponent,
    TabbedContentComponent,
    PhysicalCareComponent,
    MentalHealthComponent,
    PlayerVoiceComponent,
    PhysicalPerformanceComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot([
      {path: '', component: HomeComponent},
      {path: 'mycommunity', component: CommunityComponent}

    ]),
    BrowserAnimationsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
